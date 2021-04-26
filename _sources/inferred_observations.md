# Inferred observations

The {term}`Observation`s already described can represent the relevant information about a {doc}`system` in the form in which it is published -- but often the way we want to query it is different. For example, detailed data is published on production of many types of pharmaceuticals, but if this is too much irrelevant detail for a given study, we might prefer to query for simply the total production of all types of pharmaceuticals.

To achieve this, the {doc}`reasoning/intro` algorithm can infer new Observations from the starting ones, based on the structure of the data ({doc}`composition_equivalence`).

To distinguish between the original data and the inferred facts, datasources are entered as {term}`DirectObservation`s, while inferred facts are created as {term}`InferredObservation`.

## Concept reference

Classes:

```{glossary}
DirectObservation
  An {term}`Observation` directly derived from the data.

InferredObservation
  An {term}`Observation` inferred from other Observations.
```

Object properties:

```{glossary}
objectDirectlyDefinedBy
  Links a {term}`DirectObservation` to the {term}`Object` it describes. Subclass of {term}`objectDefinedBy`.

objectInferredDefinedBy
  Links an {term}`InferredObservation` to the {term}`Object` it describes. Subclass of {term}`objectDefinedBy`.

processDirectlyDefinedBy
  Links a {term}`DirectObservation` to the {term}`Process` it describes. Subclass of {term}`processDefinedBy`.

processInferredDefinedBy
  Links an {term}`InferredObservation` to the {term}`Process` it describes. Subclass of {term}`processDefinedBy`.
```
