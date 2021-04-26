# Developing the PRObs ontology

## Repository structure

- `docs` contains the documentation for the ontology.
- `probs_ontology` contains the actual ontology, rules and scripts.
- `probs_ontology/runner` contains Python code for setting up RDFox scripts.
- `tests` contains the tests.

## Documentation

Documentation is written using [jupyter-book](https://jupyterbook.org).

Install the Python package in a virtual environment with the necessary dependencies:

```shell
pip install -e '.[docs]'
```

## Releases

To release a new version of the ontology:

- Ensure tests are passing, documentation and changelog is up to date.

- Bump the version number according to [semantic versioning](https://semver.org/), based on the type of changes made since the last release.

- Commit the new version and tag a release like "v0.1.2"

- Build the package: `python setup.py sdist bdist_wheel`

- Publish the package to PyPI: `twine upload dist/probs_ontology-[...]`

## Tests

Install the Python package in a virtual environment:

```shell
pip install -e '.[test]'
```

Run the tests using pytest:

```shell
pytest
```

See [tests/README.md](tests/README.md) for more details of how to use the test runner.
