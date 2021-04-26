# -*- coding: utf-8 -*-

import pytest
from random import randrange, random


class TestStress:
    """Test ."""

    @pytest.fixture
    def object_facts(self):
        """These are the sample objects we will test."""
        return r"""
        :Object1 :objectComposedOf  :Object1.0 ,
                                    :Object1.1 ,
                                    :Object1.2 ,
                                    :Object1.3 ,
                                    :Object1.4 ,
                                    :Object1.5 ,
                                    :Object1.6 ,
                                    :Object1.7 ,
                                    :Object1.8 ,
                                    :Object1.9 .
        :Object2 :objectComposedOf  :Object2.0 ,
                                    :Object2.1 ,
                                    :Object2.2 ,
                                    :Object2.3 ,
                                    :Object2.4 ,
                                    :Object2.5 ,
                                    :Object2.6 ,
                                    :Object2.7 ,
                                    :Object2.8 ,
                                    :Object2.9 .
        """

    @pytest.fixture
    def obs_query(self):
        return r"""
        SELECT (COUNT(?Obs) AS ?CountObs)
        WHERE {
            ?Obs a :InferredObservation .
        }
        """

    def test_obs_1_10_1each(self, probs_facts, object_facts, make_observation, obs_query):
        """1 Object, 10 components, 1 Observation each"""

        input_obs = make_observation(object=":Object1.0", measurement=1) + \
            make_observation(object=":Object1.1", measurement=1) + \
            make_observation(object=":Object1.2", measurement=1) + \
            make_observation(object=":Object1.3", measurement=1) + \
            make_observation(object=":Object1.4", measurement=1) + \
            make_observation(object=":Object1.5", measurement=1) + \
            make_observation(object=":Object1.6", measurement=1) + \
            make_observation(object=":Object1.7", measurement=1) + \
            make_observation(object=":Object1.8", measurement=1) + \
            make_observation(object=":Object1.9", measurement=1)

        result = probs_facts(object_facts + input_obs).query_one(obs_query)

        assert result["CountObs"] == 1

    def test_obs_2_10_1each(self, probs_facts, object_facts, make_observation, obs_query):
        """2 Objects, 10 components, 1 Observation each"""

        input_obs = make_observation(object=":Object1.0", measurement=1) + \
            make_observation(object=":Object1.1", measurement=1) + \
            make_observation(object=":Object1.2", measurement=1) + \
            make_observation(object=":Object1.3", measurement=1) + \
            make_observation(object=":Object1.4", measurement=1) + \
            make_observation(object=":Object1.5", measurement=1) + \
            make_observation(object=":Object1.6", measurement=1) + \
            make_observation(object=":Object1.7", measurement=1) + \
            make_observation(object=":Object1.8", measurement=1) + \
            make_observation(object=":Object1.9", measurement=1) + \
            make_observation(object=":Object2.0", measurement=1) + \
            make_observation(object=":Object2.1", measurement=1) + \
            make_observation(object=":Object2.2", measurement=1) + \
            make_observation(object=":Object2.3", measurement=1) + \
            make_observation(object=":Object2.4", measurement=1) + \
            make_observation(object=":Object2.5", measurement=1) + \
            make_observation(object=":Object2.6", measurement=1) + \
            make_observation(object=":Object2.7", measurement=1) + \
            make_observation(object=":Object2.8", measurement=1) + \
            make_observation(object=":Object2.9", measurement=1)

        result = probs_facts(object_facts + input_obs).query_one(obs_query)

        assert result["CountObs"] == 2

    def test_obs_2_10_2each(self, probs_facts, object_facts, make_observation, obs_query):
        """2 Object, 10 components, 2 Observation each"""

        input_obs = make_observation(object=":Object1.0", measurement=1) + \
            make_observation(object=":Object1.1", measurement=1) + \
            make_observation(object=":Object1.2", measurement=1) + \
            make_observation(object=":Object1.3", measurement=1) + \
            make_observation(object=":Object1.4", measurement=1) + \
            make_observation(object=":Object1.5", measurement=1) + \
            make_observation(object=":Object1.6", measurement=1) + \
            make_observation(object=":Object1.7", measurement=1) + \
            make_observation(object=":Object1.8", measurement=1) + \
            make_observation(object=":Object1.9", measurement=1) + \
            make_observation(object=":Object1.0", measurement=2, region=":R2") + \
            make_observation(object=":Object1.1", measurement=2, region=":R2") + \
            make_observation(object=":Object1.2", measurement=2, region=":R2") + \
            make_observation(object=":Object1.3", measurement=2, region=":R2") + \
            make_observation(object=":Object1.4", measurement=2, region=":R2") + \
            make_observation(object=":Object1.5", measurement=2, region=":R2") + \
            make_observation(object=":Object1.6", measurement=2, region=":R2") + \
            make_observation(object=":Object1.7", measurement=2, region=":R2") + \
            make_observation(object=":Object1.8", measurement=2, region=":R2") + \
            make_observation(object=":Object1.9", measurement=2, region=":R2") + \
            make_observation(object=":Object2.0", measurement=1) + \
            make_observation(object=":Object2.1", measurement=1) + \
            make_observation(object=":Object2.2", measurement=1) + \
            make_observation(object=":Object2.3", measurement=1) + \
            make_observation(object=":Object2.4", measurement=1) + \
            make_observation(object=":Object2.5", measurement=1) + \
            make_observation(object=":Object2.6", measurement=1) + \
            make_observation(object=":Object2.7", measurement=1) + \
            make_observation(object=":Object2.8", measurement=1) + \
            make_observation(object=":Object2.9", measurement=1) + \
            make_observation(object=":Object2.0", measurement=2, region=":R2") + \
            make_observation(object=":Object2.1", measurement=2, region=":R2") + \
            make_observation(object=":Object2.2", measurement=2, region=":R2") + \
            make_observation(object=":Object2.3", measurement=2, region=":R2") + \
            make_observation(object=":Object2.4", measurement=2, region=":R2") + \
            make_observation(object=":Object2.5", measurement=2, region=":R2") + \
            make_observation(object=":Object2.6", measurement=2, region=":R2") + \
            make_observation(object=":Object2.7", measurement=2, region=":R2") + \
            make_observation(object=":Object2.8", measurement=2, region=":R2") + \
            make_observation(object=":Object2.9", measurement=2, region=":R2")

        result = probs_facts(object_facts + input_obs).query_one(obs_query)

        assert result["CountObs"] == 4

    def test_obs_2_10_3each(self, probs_facts, object_facts, make_observation, obs_query):
        """2 Object, 10 components, 3 Observation each"""

        input_obs = make_observation(object=":Object1.0", measurement=1) + \
            make_observation(object=":Object1.1", measurement=1) + \
            make_observation(object=":Object1.2", measurement=1) + \
            make_observation(object=":Object1.3", measurement=1) + \
            make_observation(object=":Object1.4", measurement=1) + \
            make_observation(object=":Object1.5", measurement=1) + \
            make_observation(object=":Object1.6", measurement=1) + \
            make_observation(object=":Object1.7", measurement=1) + \
            make_observation(object=":Object1.8", measurement=1) + \
            make_observation(object=":Object1.9", measurement=1) + \
            make_observation(object=":Object1.0", measurement=2, region=":R2") + \
            make_observation(object=":Object1.1", measurement=2, region=":R2") + \
            make_observation(object=":Object1.2", measurement=2, region=":R2") + \
            make_observation(object=":Object1.3", measurement=2, region=":R2") + \
            make_observation(object=":Object1.4", measurement=2, region=":R2") + \
            make_observation(object=":Object1.5", measurement=2, region=":R2") + \
            make_observation(object=":Object1.6", measurement=2, region=":R2") + \
            make_observation(object=":Object1.7", measurement=2, region=":R2") + \
            make_observation(object=":Object1.8", measurement=2, region=":R2") + \
            make_observation(object=":Object1.9", measurement=2, region=":R2") + \
            make_observation(object=":Object1.0", measurement=3, region=":R3") + \
            make_observation(object=":Object1.1", measurement=3, region=":R3") + \
            make_observation(object=":Object1.2", measurement=3, region=":R3") + \
            make_observation(object=":Object1.3", measurement=3, region=":R3") + \
            make_observation(object=":Object1.4", measurement=3, region=":R3") + \
            make_observation(object=":Object1.5", measurement=3, region=":R3") + \
            make_observation(object=":Object1.6", measurement=3, region=":R3") + \
            make_observation(object=":Object1.7", measurement=3, region=":R3") + \
            make_observation(object=":Object1.8", measurement=3, region=":R3") + \
            make_observation(object=":Object1.9", measurement=3, region=":R3") + \
            make_observation(object=":Object2.0", measurement=1) + \
            make_observation(object=":Object2.1", measurement=1) + \
            make_observation(object=":Object2.2", measurement=1) + \
            make_observation(object=":Object2.3", measurement=1) + \
            make_observation(object=":Object2.4", measurement=1) + \
            make_observation(object=":Object2.5", measurement=1) + \
            make_observation(object=":Object2.6", measurement=1) + \
            make_observation(object=":Object2.7", measurement=1) + \
            make_observation(object=":Object2.8", measurement=1) + \
            make_observation(object=":Object2.9", measurement=1) + \
            make_observation(object=":Object2.0", measurement=2, region=":R2") + \
            make_observation(object=":Object2.1", measurement=2, region=":R2") + \
            make_observation(object=":Object2.2", measurement=2, region=":R2") + \
            make_observation(object=":Object2.3", measurement=2, region=":R2") + \
            make_observation(object=":Object2.4", measurement=2, region=":R2") + \
            make_observation(object=":Object2.5", measurement=2, region=":R2") + \
            make_observation(object=":Object2.6", measurement=2, region=":R2") + \
            make_observation(object=":Object2.7", measurement=2, region=":R2") + \
            make_observation(object=":Object2.8", measurement=2, region=":R2") + \
            make_observation(object=":Object2.9", measurement=2, region=":R2") + \
            make_observation(object=":Object2.0", measurement=3, region=":R3") + \
            make_observation(object=":Object2.1", measurement=3, region=":R3") + \
            make_observation(object=":Object2.2", measurement=3, region=":R3") + \
            make_observation(object=":Object2.3", measurement=3, region=":R3") + \
            make_observation(object=":Object2.4", measurement=3, region=":R3") + \
            make_observation(object=":Object2.5", measurement=3, region=":R3") + \
            make_observation(object=":Object2.6", measurement=3, region=":R3") + \
            make_observation(object=":Object2.7", measurement=3, region=":R3") + \
            make_observation(object=":Object2.8", measurement=3, region=":R3") + \
            make_observation(object=":Object2.9", measurement=3, region=":R3")

        result = probs_facts(object_facts + input_obs).query_one(obs_query)

        assert result["CountObs"] == 6

    def test_obs_1_10_2eachsame(self, probs_facts, object_facts, make_observation, obs_query):
        """1 Object, 10 components, 2 Observation each, same probsObs"""

        input_obs = make_observation(object=":Object1.0", measurement=randrange(100000)) + \
            make_observation(object=":Object1.1", measurement=randrange(100000)) + \
            make_observation(object=":Object1.2", measurement=randrange(100000)) + \
            make_observation(object=":Object1.3", measurement=randrange(100000)) + \
            make_observation(object=":Object1.4", measurement=randrange(100000)) + \
            make_observation(object=":Object1.5", measurement=randrange(100000)) + \
            make_observation(object=":Object1.6", measurement=randrange(100000)) + \
            make_observation(object=":Object1.7", measurement=randrange(100000)) + \
            make_observation(object=":Object1.8", measurement=randrange(100000)) + \
            make_observation(object=":Object1.9", measurement=randrange(100000)) + \
            make_observation(object=":Object1.0", measurement=randrange(100000)) + \
            make_observation(object=":Object1.1", measurement=randrange(100000)) + \
            make_observation(object=":Object1.2", measurement=randrange(100000)) + \
            make_observation(object=":Object1.3", measurement=randrange(100000)) + \
            make_observation(object=":Object1.4", measurement=randrange(100000)) + \
            make_observation(object=":Object1.5", measurement=randrange(100000)) + \
            make_observation(object=":Object1.6", measurement=randrange(100000)) + \
            make_observation(object=":Object1.7", measurement=randrange(100000)) + \
            make_observation(object=":Object1.8", measurement=randrange(100000)) + \
            make_observation(object=":Object1.9",
                             measurement=randrange(100000))

        result = probs_facts(object_facts + input_obs).query_one(obs_query)

        assert result["CountObs"] == 1024

    @pytest.mark.slow
    def test_obs_2_10_2eachsame(self, probs_facts, object_facts, make_observation, obs_query):
        """2 Object, 10 components, 2 Observation each, same probsObs"""

        input_obs = make_observation(object=":Object1.0", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.1", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.2", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.3", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.4", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.5", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.6", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.7", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.8", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.9", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.0", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.1", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.2", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.3", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.4", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.5", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.6", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.7", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.8", measurement=randrange(1000000)) + \
            make_observation(object=":Object1.9", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.0", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.1", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.2", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.3", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.4", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.5", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.6", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.7", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.8", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.9", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.0", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.1", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.2", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.3", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.4", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.5", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.6", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.7", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.8", measurement=randrange(1000000)) + \
            make_observation(object=":Object2.9",
                             measurement=randrange(1000000))

        result = probs_facts(object_facts + input_obs).query_one(obs_query)

        assert result["CountObs"] == 2048

    @pytest.mark.slow
    def test_obs_1_10_3eachsame(self, probs_facts, object_facts, make_observation, obs_query):
        """
            1 Object, 10 components, 3 Observations each, same probsObs
            RDFox takes only a few seconds!
        """

        # measurement_range = 10000000000
        objects = [":Object1.0", ":Object1.1", ":Object1.2", ":Object1.3", ":Object1.4",
                   ":Object1.5", ":Object1.6", ":Object1.7", ":Object1.8", ":Object1.9"]
        input_obs = ""
        for _ in range(3):
            for obj in objects:
                # input_obs += make_observation(object=obj, measurement=randrange(measurement_range))
                input_obs += make_observation(object=obj, measurement=round(random(), 6))

        result = probs_facts(object_facts + input_obs).query_one(obs_query)

        assert result["CountObs"] == 59049

    @pytest.mark.slow
    def test_obs_2_10_3eachsame(self, probs_facts, object_facts, make_observation, obs_query):
        """
            2 Object, 10 components, 3 Observations each, same probsObs
            RDFox takes only a few seconds!
        """

        objects = [":Object1.0", ":Object1.1", ":Object1.2", ":Object1.3", ":Object1.4",
                   ":Object1.5", ":Object1.6", ":Object1.7", ":Object1.8", ":Object1.9",
                   ":Object2.0", ":Object2.1", ":Object2.2", ":Object2.3", ":Object2.4",
                   ":Object2.5", ":Object2.6", ":Object2.7", ":Object2.8", ":Object2.9"]
        input_obs = ""
        for _ in range(3):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6))

        result = probs_facts(object_facts + input_obs).query_one(obs_query)

        assert result["CountObs"] == 118098

    @pytest.mark.slow
    def test_obs_1_5_5eachsame(self, probs_facts, object_facts, make_observation, obs_query):
        """
            1 Object, 5 components, 5 Observations each, same probsObs
            RDFox takes only a few seconds!
        """

        objects = [":Object1.0", ":Object1.1",
                   ":Object1.2", ":Object1.3", ":Object1.4"]
        input_obs = ""
        for _ in range(5):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6))

        result = probs_facts(object_facts + input_obs).query_one(obs_query)

        assert result["CountObs"] == 3125

    @pytest.mark.slow
    def test_obs_1_6_6eachsame(self, probs_facts, object_facts, make_observation, obs_query):
        """
            1 Object, 6 components, 6 Observations each, same probsObs
            RDFox takes only a few seconds!
        """

        objects = [":Object1.0", ":Object1.1", ":Object1.2",
                   ":Object1.3", ":Object1.4", ":Object1.5"]
        input_obs = ""
        for _ in range(6):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6))

        result = probs_facts(object_facts + input_obs).query_one(obs_query)

        assert result["CountObs"] == 46656

    @pytest.mark.slow
    def test_obs_1_7_6eachsame(self, probs_facts, object_facts, make_observation, obs_query):
        """
            1 Object, 7 components, 6 Observations each, same probsObs
            RDFox takes only a few seconds!
        """

        objects = [":Object1.0", ":Object1.1", ":Object1.2",
                   ":Object1.3", ":Object1.4", ":Object1.5", ":Object1.6"]
        input_obs = ""
        for _ in range(6):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6))

        result = probs_facts(object_facts + input_obs).query_one(obs_query)

        assert result["CountObs"] == 279936


class TestStressMultiSteps:
    """Test ."""

    @pytest.fixture
    def object_facts_multiple_levels(self):
        """These are the sample objects we will test."""
        return r"""
        :Object1 :objectComposedOf  :Object1.1 ,
                                    :Object1.2 ,
                                    :Object1.3 ,
                                    :Object1.4 ,
                                    :Object1.5 .
        :Object1.1 :objectComposedOf    :Object1.1.1 ,
                                        :Object1.1.2 ,
                                        :Object1.1.3 ,
                                        :Object1.1.4 ,
                                        :Object1.1.5 .
        :Object1.2 :objectComposedOf    :Object1.2.1 ,
                                        :Object1.2.2 ,
                                        :Object1.2.3 ,
                                        :Object1.2.4 ,
                                        :Object1.2.5 .
        :Object1.3 :objectComposedOf    :Object1.3.1 ,
                                        :Object1.3.2 ,
                                        :Object1.3.3 ,
                                        :Object1.3.4 ,
                                        :Object1.3.5 .
        :Object1.4 :objectComposedOf    :Object1.4.1 ,
                                        :Object1.4.2 ,
                                        :Object1.4.3 ,
                                        :Object1.4.4 ,
                                        :Object1.4.5 .
        :Object1.5 :objectComposedOf    :Object1.5.1 ,
                                        :Object1.5.2 ,
                                        :Object1.5.3 ,
                                        :Object1.5.4 ,
                                        :Object1.5.5 .
        """

    @pytest.fixture
    def obs_query(self):
        return r"""
        SELECT (COUNT(?Obs) AS ?CountObs)
        WHERE {
            ?Obs a :InferredObservation .
        }
        """

    def test_obs_1_5x5_1eachsame(self, probs_facts, object_facts_multiple_levels, make_observation, obs_query):
        """
            1 Object, 5 components each with 5 components, 1 Observations each, same probsObs
            RDFox takes only a few seconds!
        """

        objects = [
            ":Object1.1",
            ":Object1.2",
            ":Object1.3",
            ":Object1.4",
            ":Object1.5",
            ":Object1.1.1",
            ":Object1.1.2",
            ":Object1.1.3",
            ":Object1.1.4",
            ":Object1.1.5",
            ":Object1.2.1",
            ":Object1.2.2",
            ":Object1.2.3",
            ":Object1.2.4",
            ":Object1.2.5",
            ":Object1.3.1",
            ":Object1.3.2",
            ":Object1.3.3",
            ":Object1.3.4",
            ":Object1.3.5",
            ":Object1.4.1",
            ":Object1.4.2",
            ":Object1.4.3",
            ":Object1.4.4",
            ":Object1.4.5",
            ":Object1.5.1",
            ":Object1.5.2",
            ":Object1.5.3",
            ":Object1.5.4",
            ":Object1.5.5"
        ]
        input_obs = ""
        for _ in range(1):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6))

        result = probs_facts(object_facts_multiple_levels + input_obs).query_one(obs_query)

        assert result["CountObs"] == 37 # 5+32

    def test_obs_1_2x2_2eachsame(self, probs_facts, object_facts_multiple_levels, make_observation, obs_query):
        """
            1 Object, 2 components each with 2 components, 2 Observations each, same probsObs
        """

        objects = [
            ":Object1.1",
            ":Object1.2",
            ":Object1.1.1",
            ":Object1.1.2",
            ":Object1.2.1",
            ":Object1.2.2"
        ]
        input_obs = ""
        for _ in range(2):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6))

        result = probs_facts(object_facts_multiple_levels + input_obs).query_one(obs_query)

        assert result["CountObs"] == 44 # 4+4+4+36-4

    def test_obs_1_3x3_2eachsame(self, probs_facts, object_facts_multiple_levels, make_observation, obs_query):
        """
            1 Object, 3 components each with 3 components, 2 Observations each, same probsObs
        """

        objects = [
            ":Object1.1",
            ":Object1.2",
            ":Object1.3",
            ":Object1.1.1",
            ":Object1.1.2",
            ":Object1.1.3",
            ":Object1.2.1",
            ":Object1.2.2",
            ":Object1.2.3",
            ":Object1.3.1",
            ":Object1.3.2",
            ":Object1.3.3"
        ]
        input_obs = ""
        for _ in range(2):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6))

        result = probs_facts(object_facts_multiple_levels + input_obs).query_one(obs_query)

        assert result["CountObs"] == 1024 # 8*3+8+1000-8

    def test_obs_1_4x4_2eachsame(self, probs_facts, object_facts_multiple_levels, make_observation, obs_query):
        """
            1 Object, 4 components each with 4 components, 2 Observations each, same probsObs
        """

        objects = [
            ":Object1.1",
            ":Object1.2",
            ":Object1.3",
            ":Object1.4",
            ":Object1.1.1",
            ":Object1.1.2",
            ":Object1.1.3",
            ":Object1.1.4",
            ":Object1.2.1",
            ":Object1.2.2",
            ":Object1.2.3",
            ":Object1.2.4",
            ":Object1.3.1",
            ":Object1.3.2",
            ":Object1.3.3",
            ":Object1.3.4",
            ":Object1.4.1",
            ":Object1.4.2",
            ":Object1.4.3",
            ":Object1.4.4"
        ]
        input_obs = ""
        for _ in range(2):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6))

        result = probs_facts(object_facts_multiple_levels + input_obs).query_one(obs_query)

        assert result["CountObs"] == 105040 # 16*4+16+104976-16

    @pytest.mark.skip(reason="our computers cannot process this, it is too big!")
    def test_obs_1_5x5_2eachsame(self, probs_facts, object_facts_multiple_levels, make_observation, obs_query):
        """
            1 Object, 5 components each with 5 components, 2 Observations each, same probsObs
            CANNOT WORK! It should create 45'435'584 of new Observations!!!
            Assuming 1 byte per character and that each observation contains around 1000 characters (I have checked this in the output of PRODCOM), only to store them we would need at least 45 GB to store them (in RAM, while processing it, they would be much more)
        """

        objects = [
            ":Object1.1",
            ":Object1.2",
            ":Object1.3",
            ":Object1.4",
            ":Object1.5",
            ":Object1.1.1",
            ":Object1.1.2",
            ":Object1.1.3",
            ":Object1.1.4",
            ":Object1.1.5",
            ":Object1.2.1",
            ":Object1.2.2",
            ":Object1.2.3",
            ":Object1.2.4",
            ":Object1.2.5",
            ":Object1.3.1",
            ":Object1.3.2",
            ":Object1.3.3",
            ":Object1.3.4",
            ":Object1.3.5",
            ":Object1.4.1",
            ":Object1.4.2",
            ":Object1.4.3",
            ":Object1.4.4",
            ":Object1.4.5",
            ":Object1.5.1",
            ":Object1.5.2",
            ":Object1.5.3",
            ":Object1.5.4",
            ":Object1.5.5"
        ]
        input_obs = ""
        for _ in range(2):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6))

        result = probs_facts(object_facts_multiple_levels + input_obs).query_one(obs_query)

        assert result["CountObs"] == 45435584 # 32*5+32+45435424-32

    @pytest.mark.slow
    def test_obs_1_3x3_3eachsame(self, probs_facts, object_facts_multiple_levels, make_observation, obs_query):
        """
            1 Object, 3 components each with 3 components, 3 Observations each, same probsObs
        """

        objects = [
            ":Object1.1",
            ":Object1.2",
            ":Object1.3",
            ":Object1.1.1",
            ":Object1.1.2",
            ":Object1.1.3",
            ":Object1.2.1",
            ":Object1.2.2",
            ":Object1.2.3",
            ":Object1.3.1",
            ":Object1.3.2",
            ":Object1.3.3"
        ]
        input_obs = ""
        for _ in range(3):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6))

        result = probs_facts(object_facts_multiple_levels + input_obs).query_one(obs_query)

        assert result["CountObs"] == 27081 # 27*3+27+27000-27

    @pytest.mark.skip(reason="our computers cannot process this, it is too big!")
    def test_obs_1_4x4_2eachsame(self, probs_facts, object_facts_multiple_levels, make_observation, obs_query):
        """
            1 Object, 4 components each with 4 components, 3 Observations each, same probsObs
            CANNOT WORK! It should create 49'787'460 of new Observations!!!
        """

        objects = [
            ":Object1.1",
            ":Object1.2",
            ":Object1.3",
            ":Object1.4",
            ":Object1.1.1",
            ":Object1.1.2",
            ":Object1.1.3",
            ":Object1.1.4",
            ":Object1.2.1",
            ":Object1.2.2",
            ":Object1.2.3",
            ":Object1.2.4",
            ":Object1.3.1",
            ":Object1.3.2",
            ":Object1.3.3",
            ":Object1.3.4",
            ":Object1.4.1",
            ":Object1.4.2",
            ":Object1.4.3",
            ":Object1.4.4"
        ]
        input_obs = ""
        for _ in range(3):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6))

        result = probs_facts(object_facts_multiple_levels + input_obs).query_one(obs_query)

        assert result["CountObs"] == 49787460 # 81*4+81+49787136-81


class TestStressMultiMultiSteps:
    """Test case of an object composed of objects, composed of objects, ... with observations only in the bottom level of this hierarcy."""

    @pytest.fixture
    def object_facts_multiple_levels(self):
        """These are the sample objects we will test."""
        return r"""
        :Object1 :objectComposedOf  :Object1.1 ,
                                    :Object1.2 ,
                                    :Object1.3 .

        :Object1.1 :objectComposedOf    :Object1.1.1 ,
                                        :Object1.1.2 ,
                                        :Object1.1.3 .
        :Object1.2 :objectComposedOf    :Object1.2.1 ,
                                        :Object1.2.2 ,
                                        :Object1.2.3 .
        :Object1.3 :objectComposedOf    :Object1.3.1 ,
                                        :Object1.3.2 ,
                                        :Object1.3.3 .

        :Object1.1.1 :objectComposedOf  :Object1.1.1.1 ,
                                        :Object1.1.1.2 ,
                                        :Object1.1.1.3 .
        :Object1.1.2 :objectComposedOf  :Object1.1.2.1 ,
                                        :Object1.1.2.2 ,
                                        :Object1.1.2.3 .
        :Object1.1.3 :objectComposedOf  :Object1.1.3.1 ,
                                        :Object1.1.3.2 ,
                                        :Object1.1.3.3 .
        :Object1.2.1 :objectComposedOf  :Object1.2.1.1 ,
                                        :Object1.2.1.2 ,
                                        :Object1.2.1.3 .
        :Object1.2.2 :objectComposedOf  :Object1.2.2.1 ,
                                        :Object1.2.2.2 ,
                                        :Object1.2.2.3 .
        :Object1.2.3 :objectComposedOf  :Object1.2.3.1 ,
                                        :Object1.2.3.2 ,
                                        :Object1.2.3.3 .
        :Object1.3.1 :objectComposedOf  :Object1.3.1.1 ,
                                        :Object1.3.1.2 ,
                                        :Object1.3.1.3 .
        :Object1.3.2 :objectComposedOf  :Object1.3.2.1 ,
                                        :Object1.3.2.2 ,
                                        :Object1.3.2.3 .
        :Object1.3.3 :objectComposedOf  :Object1.3.3.1 ,
                                        :Object1.3.3.2 ,
                                        :Object1.3.3.3 .
        """

    @pytest.fixture
    def obs_query(self):
        return r"""
        SELECT (COUNT(?Obs) AS ?CountObs)
        WHERE {
            ?Obs a :InferredObservation .
            ?Obs :objectDefinedBy :Object1 .
        }
        """

    def test_obs_obj1_comp3_obs2_min(self, probs_facts, object_facts_multiple_levels, make_observation, obs_query):
        """
            1 Object
            3 components
            2 Observations for each object at the bottom
            lower bound (non-compatible observations)
        """

        objects = [
            ":Object1.1",
            ":Object1.2",
            ":Object1.3",
        ]
        num_observations=2
        input_obs = ""
        for _ in range(num_observations):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6), region= f':R{round(random(), 6)}')

        result = probs_facts(object_facts_multiple_levels + input_obs).query_one(obs_query)

        assert result["CountObs"] == 6

    def test_obs_obj1_comp3_obs2_max(self, probs_facts, object_facts_multiple_levels, make_observation, obs_query):
        """
            1 Object
            3 components
            2 Observations for each object at the bottom
            upper bound (compatible observations)
        """

        objects = [
            ":Object1.1",
            ":Object1.2",
            ":Object1.3",
        ]
        num_observations=2
        input_obs = ""
        for _ in range(num_observations):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6))

        result = probs_facts(object_facts_multiple_levels + input_obs).query_one(obs_query)

        assert result["CountObs"] == 8

    def test_obs_obj1_comp3x3_obs2_min(self, probs_facts, object_facts_multiple_levels, make_observation, obs_query):
        """
            1 Object
            3 components each with 3 components
            2 Observations for each object at the bottom
            lower bound (non-compatible observations)
        """

        objects = [
            ":Object1.1.1",
            ":Object1.1.2",
            ":Object1.1.3",
            ":Object1.2.1",
            ":Object1.2.2",
            ":Object1.2.3",
            ":Object1.3.1",
            ":Object1.3.2",
            ":Object1.3.3",
        ]
        num_observations=2
        input_obs = ""
        for _ in range(num_observations):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6), region= f':R{round(random(), 6)}')

        result = probs_facts(object_facts_multiple_levels + input_obs).query_one(obs_query)

        assert result["CountObs"] == 18

    def test_obs_obj1_comp3x3_obs2_max(self, probs_facts, object_facts_multiple_levels, make_observation, obs_query):
        """
            1 Object
            3 components each with 3 components
            2 Observations for each object at the bottom
            upper bound (compatible observations)
        """

        objects = [
            ":Object1.1.1",
            ":Object1.1.2",
            ":Object1.1.3",
            ":Object1.2.1",
            ":Object1.2.2",
            ":Object1.2.3",
            ":Object1.3.1",
            ":Object1.3.2",
            ":Object1.3.3",
        ]
        num_observations=2
        input_obs = ""
        for _ in range(num_observations):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6))

        result = probs_facts(object_facts_multiple_levels + input_obs).query_one(obs_query)

        assert result["CountObs"] == 512

    def test_obs_obj1_comp3x3x3_obs2_min(self, probs_facts, object_facts_multiple_levels, make_observation, obs_query):
        """
            1 Object
            3 components each with 3 components each with 3 components
            2 Observations for each object at the bottom
            lower bound (non-compatible observations)
        """

        objects = [
            ":Object1.1.1.1",
            ":Object1.1.1.2",
            ":Object1.1.1.3",
            ":Object1.1.2.1",
            ":Object1.1.2.2",
            ":Object1.1.2.3",
            ":Object1.1.3.1",
            ":Object1.1.3.2",
            ":Object1.1.3.3",
            ":Object1.2.1.1",
            ":Object1.2.1.2",
            ":Object1.2.1.3",
            ":Object1.2.2.1",
            ":Object1.2.2.2",
            ":Object1.2.2.3",
            ":Object1.2.3.1",
            ":Object1.2.3.2",
            ":Object1.2.3.3",
            ":Object1.3.1.1",
            ":Object1.3.1.2",
            ":Object1.3.1.3",
            ":Object1.3.2.1",
            ":Object1.3.2.2",
            ":Object1.3.2.3",
            ":Object1.3.3.1",
            ":Object1.3.3.2",
            ":Object1.3.3.3",
        ]
        num_observations=2
        input_obs = ""
        for _ in range(num_observations):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6), region= f':R{round(random(), 6)}')

        # print(object_facts_multiple_levels + input_obs)

        result = probs_facts(object_facts_multiple_levels + input_obs).query_one(obs_query)

        assert result["CountObs"] == 54

    @pytest.mark.skip(reason="our computers cannot process this, it is too big!")
    def test_obs_obj1_comp3x3x3_obs2_max(self, probs_facts, object_facts_multiple_levels, make_observation, obs_query):
        """
            1 Object
            3 components each with 3 components each with 3 components
            2 Observations for each object at the bottom
            upper bound (compatible observations)
        """

        objects = [
            ":Object1.1.1.1",
            ":Object1.1.1.2",
            ":Object1.1.1.3",
            ":Object1.1.2.1",
            ":Object1.1.2.2",
            ":Object1.1.2.3",
            ":Object1.1.3.1",
            ":Object1.1.3.2",
            ":Object1.1.3.3",
            ":Object1.2.1.1",
            ":Object1.2.1.2",
            ":Object1.2.1.3",
            ":Object1.2.2.1",
            ":Object1.2.2.2",
            ":Object1.2.2.3",
            ":Object1.2.3.1",
            ":Object1.2.3.2",
            ":Object1.2.3.3",
            ":Object1.3.1.1",
            ":Object1.3.1.2",
            ":Object1.3.1.3",
            ":Object1.3.2.1",
            ":Object1.3.2.2",
            ":Object1.3.2.3",
            ":Object1.3.3.1",
            ":Object1.3.3.2",
            ":Object1.3.3.3",
        ]
        num_observations=2
        input_obs = ""
        for _ in range(num_observations):
            for obj in objects:
                input_obs += make_observation(object=obj, measurement=round(random(), 6))

        result = probs_facts(object_facts_multiple_levels + input_obs).query_one(obs_query)

        assert result["CountObs"] == 134217728

