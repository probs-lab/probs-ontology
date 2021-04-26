# -*- coding: utf-8 -*-

import re
from pathlib import Path
import pytest

from probs_ontology.runner.datasource import Datasource, load_datasource


class TestDatasourceCreatedManually:

    @pytest.fixture
    def datasource(self):
        return Datasource.from_facts(":Farming a :Process .")

    def test_has_load_data(self, datasource):
        match = re.match(r"import (.*)", datasource.load_data_script)
        assert match
        filename = f"data/{match.group(1)}"
        assert filename in datasource.input_files
        # check contents
        contents = datasource.input_files[filename].read()
        assert contents == ":Farming a :Process ."

    def test_has_no_rules(self, datasource):
        assert datasource.rules == ""


class TestDatasourceFromFolder:
    DATASOURCE_FOLDER = Path(__file__).parent / "sample_datasource_simple"

    @pytest.fixture
    def datasource(self):
        return load_datasource(self.DATASOURCE_FOLDER)

    def test_has_load_data(self, datasource):
        assert datasource.load_data_script.startswith("prefix ufrd:")

    def test_has_rules(self, datasource):
        assert datasource.rules.startswith(":Object[?ObjectID]")

    def test_has_input_files(self, datasource):
        assert datasource.input_files == {
            "data/sample_datasource_simple/data.csv": self.DATASOURCE_FOLDER / "data.csv"
        }


def test_datasource_errors_for_missing_folder():
    with pytest.raises(NotADirectoryError):
        load_datasource(Path("MISSING_FOLDER"))
