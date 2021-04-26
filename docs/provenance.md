# Provenance

It's important to keep track of where *Observations* have come from, in order to
- correctly attribute data sources
- check that two pieces of information are truely independent, and not both secondary reports of the same primary source
- understand where results have come from

## Class reference

Dataset
: A collection of {term}`Observation`s. Example: the 2018 PRODCOM dataset.

## Property reference

Object properties:

partOfDataset
: Links an Observation to the Dataset it is part of.

prov:wasDerivedFrom
: Links an InferredObservation to the Observation is derives from.

