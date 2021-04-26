# pytest unit tests

The tests in this directory are unit tests for the ontology, based on [pytest](https://docs.pytest.org/en/stable/).

To run all the tests:

``` shell
pytest
```

To run a subset of tests use `-k` to filter, for example:
``` shell
pytest -k basic
```
runs only tests with "basic" in their filename, classname or test name.

## More information about failing tests

Print the input facts supplied to RDFox and the full set of facts that were inferred:
``` shell
pytest --print-facts
```
(this could be a lot of output for a large test case)

Show more detail including output from RDFox:
``` shell
pytest --log-level DEBUG
```
(other log levels such as INFO can also be used)

If the log level is set to at least INFO, it will print the temporary directory that was set up for RDFox to run. You can go to this path to check in more detail what's happening in the test.

You can also manually specify the path to the working directory with `pytest --working-dir <...>` but you are then responsible for making sure it is clean before each run -- do this only when running a single test at a time.

**Note**: occasionally pytest complains that the arguments `--print-facts` and `--working-dir` are not defined. If this happens, run pytest from within the "Ontologies/tests" directory, or pass it that path to that directory (e.g. `pytest tests/ -k basic`) 

## Other pytest options

Pytest has lots of convenient ways to choose the tests to run; see its documentation for more details.

Useful options include:
- `-x` to stop after the first failed test
- `--lf` to rerun only the tests that failed last time
- `--nf` to run newly added tests first

## How it works

The `conftest.py` file is run by pytest to set up all tests in this directory. It defines the custom options `--print-facts` and `--working-dir`, and defines some "fixtures" for use by tests. [Fixtures](https://docs.pytest.org/en/stable/fixture.html) are objects or functions that can are provided to individual test cases by listing their names in the tests' arguments list.

The main fixture for running RDFox is `probs_facts`. This provides a function which takes some TTL facts as a string, and returns a `ProbsFacts` object with a method `query()` which runs RDFox and returns the result. 

Another useful fixture is `make_observation`, which returns a function for constructing Observation data with default values for anything not specified.
