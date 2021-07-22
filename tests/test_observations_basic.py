# -*- coding: utf-8 -*-

from decimal import Decimal
import pytest

from probs_runner import PROBS


@pytest.fixture
def cake_facts():
    facts = r"""
:Cake a :Object ;
    :objectName "Cake" .
:Torta a :Object ;
    :objectName "Torta" .
:Obs1 a :Observation ;
    :hasRole :SoldProduction ;
    :objectDefinedBy :Cake ;
    :hasTimePeriod :YearOf2018 ;
    :hasRegion :UnitedKingdom ;
    :metric "mass" ;
    :bound :ExactBound ;
    :measurement 15.4 .
"""
    return facts


def test_basic_observations(probs_facts, cake_facts):
    """This is not a very good test, but checks everything is running ok."""
    result = probs_facts(cake_facts).query_one(
        r"""
        SELECT ?role ?measurement WHERE {
          :Obs1 :hasRole ?role ;
          :measurement ?measurement .
        }
        """
    )
    assert result["role"] == PROBS.SoldProduction
    assert result["measurement"] == Decimal('15.4')


class TestObservationEquivalence:
    """Test effect of :objectEquivalentTo on Observations"""

    def test_no_observation_without_equivalence(self, probs_facts, cake_facts):
        """When two objects not equivalent, observations should not be inferred across."""
        result = probs_facts(cake_facts).query(
            r"""SELECT ?obs WHERE { ?obs :objectDefinedBy :Torta . }"""
        )
        assert len(result) == 0

    def test_there_is_observation_with_equivalence(self, probs_facts, cake_facts):
        """When two objects are equivalent, observations should be inferred across."""
        equivalence = ":Cake :objectEquivalentTo :Torta ."
        result = probs_facts(cake_facts + equivalence).query_one(
            r"""SELECT ?obs WHERE { ?obs :objectDefinedBy :Torta . }"""
        )
        assert result["obs"] == PROBS.Obs1

    def test_observation_with_equivalence_has_bound(self, probs_facts, cake_facts):
        equivalence = ":Cake :objectEquivalentTo :Torta ."
        result = probs_facts(cake_facts + equivalence).query_one(
            r"""SELECT ?obs ?bound WHERE { ?obs :objectDefinedBy :Torta ; :bound ?bound . }"""
        )
        assert result["bound"] == PROBS.ExactBound


class TestObservationCompositionWithCompatibleObservations:
    """When an Object is composed of other objects, the measurements of compatible
    objects should be summed.

    """

    @pytest.fixture
    def baked_goods_facts(self):
        """These are the sample objects we will test."""
        return r"""
        :Cake a :Object .
        :Bread a :Object .
        :BakedGoods a :Object .
        :BakedGoods :objectComposedOf :Cake, :Bread .
        """

    @pytest.fixture
    def obs_query(self):
        return r"""
        SELECT ?obs ?role ?time ?region ?metric ?measurement ?bound
        WHERE {
            ?obs :objectDefinedBy :BakedGoods ;
            :hasRole ?role ;
            :hasTimePeriod ?time ;
            :hasRegion ?region ;
            :metric ?metric ;
            :measurement ?measurement ;
            :bound ?bound .
        }
        ORDER BY ?role ?time ?region ?metric
        """

    def test_two_compatible_observations_are_summed(
        self, probs_facts, baked_goods_facts, make_observation, obs_query
    ):
        result = probs_facts(
            baked_goods_facts
            + make_observation(object=":Cake", measurement=5.1)
            + make_observation(object=":Bread", measurement=22.6)
        ).query_one(obs_query)

        assert result["obs"].startswith(
            "https://ukfires.org/probs/ontology/ComposedInferredObservation-"
        )
        assert result["role"] == PROBS.SoldProduction
        assert result["time"] == PROBS.YearOf2018
        assert result["region"] == PROBS.UnitedKingdom
        assert result["metric"] == "mass"
        assert result["measurement"] == Decimal("27.7")
        assert result["bound"] == PROBS.ExactBound

    def test_compatible_sets_of_observations_are_summed_separately(
        self, probs_facts, baked_goods_facts, make_observation, obs_query
    ):
        """Like the previous test, but now with some observations from 2019 too."""
        result = probs_facts(
            baked_goods_facts
            + make_observation(time=":YearOf2018", object=":Cake", measurement=5.1)
            + make_observation(time=":YearOf2018", object=":Bread", measurement=22.6)
            + make_observation(time=":YearOf2019", object=":Cake", measurement=3.1)
            + make_observation(time=":YearOf2019", object=":Bread", measurement=20.0)
        ).query(obs_query)

        to_check = [(x["time"], x["measurement"], x["bound"]) for x in result]
        assert to_check == [
            (PROBS.YearOf2018, Decimal("27.7"), PROBS.ExactBound),
            (PROBS.YearOf2019, Decimal("23.1"), PROBS.ExactBound),
        ]

    def test_observations_with_different_roles_are_not_composed(
        self, probs_facts, baked_goods_facts, make_observation, obs_query
    ):
        """Different roles are not compatible -- only lower bounds are inferred for
        BakedGoods."""
        result = probs_facts(
            baked_goods_facts
            + make_observation(object=":Bread", role=":Import", measurement=3.2)
            + make_observation(object=":Cake", role=":SoldProduction", measurement=5.4)
        ).query(obs_query)

        to_check = [(x["role"], x["measurement"], x["bound"]) for x in result]
        assert to_check == [
            (PROBS.Import, Decimal("3.2"), PROBS.LowerBound),
            (PROBS.SoldProduction, Decimal("5.4"), PROBS.LowerBound),
        ]

    def test_observations_with_different_time_periods_are_not_composed(
        self, probs_facts, baked_goods_facts, make_observation, obs_query
    ):
        """Different time periods are not compatible."""
        result = probs_facts(
            baked_goods_facts
            + make_observation(object=":Cake", time=":YearOf2018", measurement=3.2)
            + make_observation(object=":Bread", time=":YearOf2019", measurement=5.4)
        ).query(obs_query)

        to_check = [(x["time"], x["measurement"], x["bound"]) for x in result]
        assert to_check == [
            (PROBS.YearOf2018, Decimal("3.2"), PROBS.LowerBound),
            (PROBS.YearOf2019, Decimal("5.4"), PROBS.LowerBound),
        ]

    def test_observations_with_different_regions_are_not_composed(
        self, probs_facts, baked_goods_facts, make_observation, obs_query
    ):
        """Different regions are not compatible."""
        result = probs_facts(
            baked_goods_facts
            + make_observation(object=":Bread", region=":Italy", measurement=3.2)
            + make_observation(object=":Cake", region=":UnitedKingdom", measurement=5.4)
        ).query(obs_query)

        to_check = [(x["region"], x["measurement"], x["bound"]) for x in result]
        assert to_check == [
            (PROBS.Italy, Decimal("3.2"), PROBS.LowerBound),
            (PROBS.UnitedKingdom, Decimal("5.4"), PROBS.LowerBound),
        ]

    def test_observations_with_different_metrics_are_not_composed(
        self, probs_facts, baked_goods_facts, make_observation, obs_query
    ):
        """Different metrics are not compatible."""
        result = probs_facts(
            baked_goods_facts
            + make_observation(object=":Cake", metric='"mass"', measurement=3.2)
            + make_observation(object=":Bread", metric='"volume"', measurement=5.4)
        ).query(obs_query)

        to_check = [(x["metric"], x["measurement"], x["bound"]) for x in result]
        assert to_check == [
            ("mass", Decimal("3.2"), PROBS.LowerBound),
            ("volume", Decimal("5.4"), PROBS.LowerBound),
        ]


class TestObservationCompositionMultipleSteps:
    """Test longer chains of inferred observations."""

    @pytest.fixture
    def object_facts(self):
        """These are the sample objects we will test."""
        return r"""
        :Cupcakes a :Object .
        :Muffins a :Object .
        :Cake a :Object .
        :Bread a :Object .
        :BakedGoods a :Object .

        :BakedGoods :objectComposedOf :Cake, :Bread .
        :Cake :objectComposedOf :Cupcakes, :Muffins .
        """

    @pytest.fixture
    def all_facts(self, object_facts, make_observation):
        """Sample data about the objects."""
        return (
            object_facts
            + make_observation(object=":Cupcakes", measurement=2)
            + make_observation(object=":Muffins", measurement=3)
            + make_observation(object=":Bread", measurement=6)
        )

    def test_observations_are_summed_across_multiple_steps(self, probs_facts, all_facts):
        result = probs_facts(all_facts).query("""
        SELECT ?measurement ?bound
        WHERE {
            ?obs :objectDefinedBy :BakedGoods ;
                 :measurement ?measurement ;
                 :bound ?bound .
        }
        ORDER BY ?measurement
        """)

        assert result == [
            {"bound": PROBS.ExactBound, "measurement": 11},
        ]

    def test_observation_was_derived_from(self, probs_facts, all_facts):
        result = probs_facts(all_facts).query("""
            PREFIX prov: <http://www.w3.org/ns/prov#>
            SELECT ?obs ?WDF
            WHERE {
                ?obs    :objectDefinedBy    :BakedGoods ;
                    prov:wasDerivedFrom     ?WDF .
            }
            ORDER BY ?WDF
            """)

        import re
        direct_obs = set(map('https://ukfires.org/probs/ontology/'.__add__,
                             re.findall('(Obs.*?) a :DirectObservation', all_facts, re.DOTALL)))

        assert len(result) == 3
        assert len(set(x["obs"] for x in result)) == 1
        assert set(str(x["WDF"]) for x in result) == direct_obs

    def test_only_one_exact_observations_at_top_level(self, probs_facts, all_facts):
        result = probs_facts(all_facts).query("""
        SELECT ?measurement
        WHERE {
            ?obs :objectDefinedBy :BakedGoods ;
                 :measurement ?measurement ;
                 :bound :ExactBound .
        }
        ORDER BY ?measurement
        """)

        assert result == [
            {"measurement": 11},
        ]


class TestLowerBounds:
    """When an Object is composed of other objects, inferred observations should be
    marked as lower bounds if any observations are missing.

    """

    @pytest.fixture
    def baked_goods_facts(self):
        """These are the sample objects we will test."""
        return r"""
        :Cake a :Object .
        :Bread a :Object .
        :BakedGoods a :Object .
        :BakedGoods :objectComposedOf :Cake, :Bread .
        """

    @pytest.fixture
    def obs_query(self):
        return r"""
        SELECT ?measurement ?bound
        WHERE {
            ?obs :objectDefinedBy :BakedGoods ;
                 :measurement ?measurement ;
                 :bound ?bound .
        }
        ORDER BY ?measurement ?bound
        """

    def test_nothing_is_inferred_with_no_inputs(
        self, probs_facts, baked_goods_facts, obs_query
    ):
        # This is a fairly trivial test, but just to check...
        result = probs_facts(baked_goods_facts).query(obs_query)
        assert len(result) == 0

    def test_lower_bound_is_inferred_with_missing_observation(
        self, probs_facts, baked_goods_facts, make_observation, obs_query
    ):
        result = probs_facts(
            baked_goods_facts
            + make_observation(object=":Cake", measurement=5.1)
            # no observation for bread
        ).query(obs_query)

        assert result == [
            {"bound": PROBS.LowerBound, "measurement": Decimal("5.1")},
        ]

    def test_lower_bound_is_inferred_with_missing_measurement(
        self, probs_facts, baked_goods_facts, make_observation, obs_query
    ):
        result = probs_facts(
            baked_goods_facts
            + make_observation(object=":Cake", measurement=5.1)
            + make_observation(object=":Bread", measurement=None)
        ).query(obs_query)

        assert result == [
            {"bound": PROBS.LowerBound, "measurement": Decimal("5.1")},
        ]

    def test_exact_bound_is_inferred_with_zero_measurement(
        self, probs_facts, baked_goods_facts, make_observation, obs_query
    ):
        result = probs_facts(
            baked_goods_facts
            + make_observation(object=":Cake", measurement=5.1)
            + make_observation(object=":Bread", measurement=0)
        ).query(obs_query)

        assert result == [
            {"bound": PROBS.ExactBound, "measurement": Decimal("5.1")},
        ]
