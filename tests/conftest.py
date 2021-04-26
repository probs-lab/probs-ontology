"""Common configuration shared by all tests in this directory."""


from uuid import uuid4
from pathlib import Path
import pytest

from probs_ontology import ProbsFacts


def pytest_addoption(parser):
    parser.addoption(
        "--print-facts", action="store_true", help="enable dumping the facts"
    )
    parser.addoption(
        "--working-dir", action="store", help="path to working directory, default temporary"
    )
    parser.addoption(
        "--ontology-dir", action="store", help="path to ontology scripts, default ../probs_ontology relative to tests"
    )
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


@pytest.fixture
def probs_facts(request, tmp_path):
    """Return a function to run a set of facts"""
    print_facts = request.config.getoption("--print-facts")
    working_dir = request.config.getoption("--working-dir") or tmp_path
    source_dir = request.config.getoption("--ontology-dir")
    if source_dir:
        source_dir = Path(source_dir)
    else:
        source_dir = Path(__file__).parent.parent / "probs_ontology"

    # Return a more verbose function if requested by the command-line argument.
    if print_facts:
        def probs_facts_func(facts):
            print("Facts:")
            print(facts)
            return ProbsFacts(facts, print_facts=True, working_dir=working_dir, script_source_dir=source_dir)
    else:
        def probs_facts_func(facts):
            return ProbsFacts(facts, print_facts=False, working_dir=working_dir, script_source_dir=source_dir)

    return probs_facts_func


@pytest.fixture
def default_observation_params():
    """These are the default parameters for defining Observations for testing, which
    can be overridden as needed."""
    return {
        "role": ":SoldProduction",
        "time": ":YearOf2018",
        "region": ":UnitedKingdom",
        "metric": '"mass"',
        "measurement": 1.0,
    }


@pytest.fixture
def make_observation(default_observation_params):
    """Provide a function to create an Observation."""

    def func(**params):
        # Use defaults, overridden as needed
        params = {**default_observation_params, **params}
        obs_id = uuid4()
        elements = [
            f":Obs{obs_id} a :DirectObservation",
            ":bound :ExactBound"
        ]
        if params["role"] is not None:
            elements.append(f":hasRole {params['role']}")
        if params["object"] is not None:
            elements.append(f":objectDefinedBy {params['object']}")
        if params["time"] is not None:
            elements.append(f":hasTimePeriod {params['time']}")
        if params["region"] is not None:
            elements.append(f":hasRegion {params['region']}")
        if params["metric"] is not None:
            elements.append(f":metric {params['metric']}")
        if params["measurement"] is not None:
            elements.append(f":measurement {params['measurement']}")
        return " ; ".join(elements) + " .\n"

    return func
