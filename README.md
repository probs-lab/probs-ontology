# PRObs ontology

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5052738.svg)](https://doi.org/10.5281/zenodo.5052738)

This repository contains the "Physical Resources Observatory" (PRObs) ontology. It includes definitions of the concepts and relations as an OWL ontology in TTL format, as well as a version converted to Datalog rules and RDF data designed to be run with the [RDFox triple store](https://www.oxfordsemantic.tech/product). 

This ontology is being developed as part of [UK FIRES](https://ukfires.org).

## Getting started

See the [documentation](https://probs-ontology.netlify.app/) for more information about the ontology concepts and how it can be used.

You can obtain a copy of the ontology files from this git repository, or get the converted ontology files by installing the Python package `probs_module_ontology`.

[TODO: update this example for v2 -- See [probs-ontology-example](https://github.com/ukfires/probs-ontology-example/) for a practical example of using the PRObs system to access resource data.]

[TODO: add links to probs-runner and the other modules].

## Custom builds of the ontology including additional data / external ontologies

We build a version of the PRObs ontology bundled with the core external ontologies (PROV, QUDT) that are used with it, for convenience in loading into tools such as RDFox.

If you want to use additional ontologies or data (e.g. details of specific time periods or regions where your data is measured), you may find it useful to create a custom build by modifying the ontologies in the `conversion` subfolder. See [DEVELOPING.md](DEVELOPING.md) for more information.

## Contributing 🎁

Contributions are welcome: share examples of work done using the ontology, make suggestions for improving the documentation, and examples of things that are more difficult than they should be or don't work -- as well as of course making actual fixes to the definitions, scripts and documentation.

See [DEVELOPING.md](DEVELOPING.md) for more information

## Authors

- Stefano Germano
- Carla Saunders
- Rick Lupton

## License

The PRObs ontology is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
