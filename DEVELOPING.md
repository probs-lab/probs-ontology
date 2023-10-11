# Developing the PRObs ontology

## Repository structure

- `docs` contains the documentation for the ontology.
- `ontology` contains the actual ontology definitions.
- `spec` contains generated documentation.
- `conversion` contains scripts and additional ontologies that are convenient to bundle with the PRObs ontology for further processing/reasoning.

## Documentation

Documentation is written using [jupyter-book](https://jupyterbook.org).

You can create a Conda environment with the necessary tools installed using:

```shell
conda env create
conda activate probs-ontology
```

Additional documentation is generated from the ontology definitions in the
`spec` folder.

## Releases

To release a new version of the ontology:

- Ensure documentation and changelog are up to date.

- Bump the version number according to [semantic versioning](https://semver.org/), based on the type of changes made since the last release.

- Commit the new version and tag a release like "v0.1.2"
