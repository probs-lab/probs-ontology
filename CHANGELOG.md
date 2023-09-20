<!-- markdownlint-configure-file {"MD024": { "siblings_only": true } } -->

# Changelog

All notable changes to our ontologies will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0).

---

## PROBS (`probs.ttl`)

### [2.0.0] - 2023-01-27

#### Changed

- `:metric` -> `:hasMetric`
- `:bound` -> `:hasBound`
- `:hasTimePeriod` range to `time:TemporalEntity`
- `:hasTimePeriod` -> `:hasTime`
- `:belongsToList` -> `:partOfList`
- `:objectName` -> `rdfs:label`
- `:processName` -> `rdfs:label`
- `:codeName` -> `rdfs:label`
- `:metricName` -> `rdfs:label`

#### Removed

- `ufpc:ClassificationCode`
- `ufct:ClassificationCode`
- `ufpc:ClassificationCodeList`
- `ufct:ClassificationCodeList`
- Unused prefixes

### [1.5.2] - 2021-04-16

#### Removed

- Unused triples

### [1.5.1] - 2021-04-16

#### Changed

- Fixed prefixes

### [1.5.0] - 2021-04-16

#### Added

- GeoNames
- OWL-Time

#### Removed

- `:TimePeriod`
- `:Region`

### [1.4.0] - 2021-04-12

#### Added

- `:Metric` concept
- `metricName` relation for `Metric`
- `:processEquivalentTo`relation for `Process`

#### Changed

- `:metric` relation for `Metric` to owl:ObjectProperty

### [1.3.0] - 2020-01-04

#### Changed

- `:wasDerivedFrom` to `prov:wasDerivedFrom`
- `:Object` and `Observation` as `rdfs:subClassOf` of `prov:Entity`

### [1.2.0] - 2021-03-30

#### Added

- `:MeasurementBound` concept
- `bound` relation for `Observation`

### [1.1.0] - 2020-12-03

#### Added

- `processName` and `processDescription` relations for `Process`

### [1.0.0] - 2020-11-23

#### Added

- `Role` concept and hierarchy
- `hasRole` relation from `Observation` to `Role`
- `consumes` and `produces` relations from `Process` to `Object`

#### Changed

- Transformed one of the two hierarchies of `Observation` into `Role` (see #89)
- `FlowObservation`, `StockObservation` and all their sub-classes into sub-classes of `Role`

### [0.6.0] - 2020-10-27

#### Added

- `metric`
- `objectEquivalentTo` as equivalence relation

#### Changed

- `objectDefinedBy` domains

#### Removed

- `Measurement` concept
- `hasMeasurement` relation

### [0.5.0] - 2020-10-17

#### Added

- Sub-properties of `objectDefinedBy` (#74)
- `wasDerivedFrom` property (#74)

### [0.4.1] - 2020-10-16

#### Changed

- Improved labels

### [0.4.0] - 2020-10-16

#### Removed

- Unneeded relations (#80)

### [0.3.0] - 2020-10-09

#### Changed

- Base IRI to UK FIRES website (#63)

### [0.2.0] - 2020-10-02

#### Added

- Additional information for the ontology
- Version of the ontology

#### Changed

- Ontology base IRI and prefixes
- Format of the triples

---

## PRODCOM (`prodcom.ttl`)

??
