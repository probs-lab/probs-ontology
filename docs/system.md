# Material flow systems

The core conceptual model is consistent with the *bipartite directed graphs* described by {cite}`pauliuk_practical_2016`:
- A *Process* is where events/transformations happen. Inputs and outputs.
- The things going in and out are *Objects* (taken broadly, to include goods, materials, energy and services).
- A *flow* is the movement of an object in or out of a process.

A material flow system consists of a set of processes within a boundary, defined in both space and time. 

## Concept reference

Classes:

```{glossary}
Process
    One or more grouped operations in a system that can be defined and separated from others. A Process has an input of some Object(s) and an output of some Object(s)

Object
    A type of thing; what is flowing in a Flow, or accumulated in a Stock. This is a more general term that includes Goods and Substances, but also non-material things such as energy and services.
```

Object properties:

```{glossary}
consumes
  Links a Process to an Object that it consumes as an input

produces
  Links a Process to an Object that it produces as an output
```

Data properties:

```{glossary}
objectName
  Links an Object to its human-readable name

objectDescription
  Links an Object to a human-readable description of that object

processName
  Links a Process to its human-readable name

processDescription
  Links a Process to a human-readable description of that process
```
