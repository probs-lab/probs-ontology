#!/usr/bin/env python3


from hashlib import md5
from pathlib import Path
from io import StringIO


class Datasource:
    def __init__(self, input_files=None, load_data_script="", rules=""):
        if input_files is None:
            input_files = {}
        self.input_files = input_files
        self.load_data_script = load_data_script
        self.rules = rules

    @classmethod
    def from_facts(cls, facts):
        """Create a datasource from explicit list of facts."""
        hash = md5(facts.encode()).hexdigest()
        input_files = {
            f"data/{hash}.ttl": StringIO(facts)
        }
        import_statement = f"import {hash}.ttl\n"
        return cls(input_files, import_statement)


def load_datasource(path: Path):
    if not path.is_dir():
        raise NotADirectoryError(path)

    load_data_path = path / "load_data.rdfox"
    if load_data_path.exists():
        load_data_script = load_data_path.read_text()
    else:
        load_data_script = ""

    map_path = path / "map.dlog"
    if map_path.exists():
        rules = map_path.read_text()
    else:
        rules = ""

    data_files = path.glob("*.csv")
    datasource_name = path.stem
    input_files = {
        f"data/{datasource_name}/{filename.relative_to(path)}": filename
        for filename in data_files
    }

    return Datasource(input_files, load_data_script, rules)
