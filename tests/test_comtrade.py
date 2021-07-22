# -*- coding: utf-8 -*-

from decimal import Decimal
from math import isnan
from pathlib import Path
import pytest
import csv
from io import StringIO

from probs_runner import load_datasource


def limit_to_rows_matching_prefix(infile, outfile, column, prefix):
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    writer.writerow(next(reader))  # header
    for row in reader:
        if row[column].startswith(prefix):
            writer.writerow(row)


def comtrade_datasource_limited_to_prefix(prefix):
    source = load_datasource(Path(__file__).parent / "testing_datasources/COMTRADE")

    # Replace the data with a subset having only the codes matching the given
    # prefix
    CODE_COLUMN = 22
    for tgt, src in source.input_files.items():
        if src.name == "ct-2018-imports.csv":
            data = StringIO(newline="")
            with open(src, "rt", newline="") as f:
                limit_to_rows_matching_prefix(f, data, CODE_COLUMN, prefix)
            data.seek(0)
            source.input_files[tgt] = data

    return source


class TestCOMTRADECodes105:
    # TODO The intention of writing it like this is to make it more efficient by
    # answering all three queries at once, but currently it doesn't do that
    # because probs_fact fixture uses tmp_path fixture, which is scoped to each
    # test function.
    @pytest.fixture
    def queries(self, probs_facts):
        source = comtrade_datasource_limited_to_prefix("105")
        return probs_facts([source]).query({
            "objects": r"""
            SELECT ?Object ?ObjectName ?ParentName
            WHERE {
                ?Object a :Object .
                OPTIONAL { ?Object :objectName ?ObjectName }.
                OPTIONAL { ?Parent :objectComposedOf ?Object ; :objectName ?ParentName }.
            }
            ORDER BY ?ObjectName
            """,

            "object_directobs": r"""
            SELECT ?ObjectName ?Measurement
            WHERE {
                ?Object a :Object ; :objectName ?ObjectName .
                FILTER( STRSTARTS(?ObjectName, "COMTRADE Object from Code 105") ||
                        ?ObjectName = "COMTRADE Object from Code 1" ||
                        ?ObjectName = "COMTRADE Object from Code TOTAL" )
                OPTIONAL { ?Obs a :DirectObservation ;
                                  :objectDefinedBy ?Object ;
                                  :measurement ?Measurement . }
            }
            ORDER BY ?ObjectName
            """,

            "inferredobs": r"""
            SELECT ?Obs ?ObjectName ?Measurement
            WHERE {
                ?Obs a :InferredObservation ;
                     :objectDefinedBy [ :objectName ?ObjectName ] ;
                     :measurement ?Measurement
            }
            ORDER BY ?ObjectName
            """
        })

    @pytest.mark.xfail(reason="extra unnamed parent object is created")
    def test_expected_number_of_objects(self, queries):
        result = queries["objects"]
        assert len(result) == 8

    def test_expected_direct_observations(self, queries):
        result = queries["object_directobs"]
        to_check = [(row["ObjectName"], row["Measurement"]) for row in result]
        assert to_check == [
            ('COMTRADE Object from Code 1', None),
            ('COMTRADE Object from Code 105', 0.0),
            ('COMTRADE Object from Code 10511', 52650005.0),
            ('COMTRADE Object from Code 10512', 0.0),
            ('COMTRADE Object from Code 10513', 5910.0),
            ('COMTRADE Object from Code 10514', None),
            ('COMTRADE Object from Code 10515', None),
            ('COMTRADE Object from Code 10594', 62417.0),
            ('COMTRADE Object from Code 10599', None),
            ('COMTRADE Object from Code TOTAL', None)
        ]

    def test_expected_number_of_inferred_observations(self, queries):
        result = queries["inferredobs"]
        to_check = [(row["ObjectName"], row["Measurement"]) for row in result]
        assert to_check == [
            ('COMTRADE Object from Code 1', 0),              # 2a. inferred from direct obs on 105
            ('COMTRADE Object from Code 1', 52718332),       # 2b. inferred from (1)
            ('COMTRADE Object from Code 105', 52718332),     # 1.  sum of direct, lower bound
            ('COMTRADE Object from Code TOTAL', 52718332),   # 3a. inferred from (2b)
            ('COMTRADE Object from Code TOTAL', 0)           # 3b. inferred from (2a)
        ]
