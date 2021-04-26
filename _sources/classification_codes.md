# Classification codes

Formal classification codes such as the [Combined Nomenclature (CN)](https://ec.europa.eu/taxation_customs/business/calculation-customs-duties/what-is-common-customs-tariff/combined-nomenclature_en) can play an important role in structuring information about *Objects* and *Processes*.

## Class reference

ClassificationCode
: An entry within a ClassificationCodeList. Example: `10.11.11.40` in the 2017-18 PRODCOM list.

ClassificationCodeList
: A set of ClassificationCodes. Example: the 2017-18 PRODCOM list, or the 2020 CN list.

## Property reference

Object properties:

belongsToList
: Links a ClassificationCode to a ClassificationCodeList. For example, `CN2020_1806.10.15 :belongsToList :CN2020`.

hasClassificationCode
: Links an Object to an associated ClassificationCode.

Data properties:

codeName
: Links a ClassificationCode to its human-readable code name.

codeDescription
: Links a ClassificationCode to its human-readable description, which usually forms the definition of the code in the ClassificationCodeList.
