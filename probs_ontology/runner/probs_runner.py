"""Functions for running RDFox with necessary input files and scripts, and
collecting results.

This aims to hide the complexity of setting up RDFox, loading data, adding
rules, answering queries, behind a simple function that maps data -> answers.
"""


from contextlib import contextmanager
import logging
from typing import Dict, ContextManager, Iterator
from io import StringIO
import importlib_resources
import shutil
import pandas as pd
from rdflib import Namespace
from rdflib.namespace import RDF, RDFS

from rdfox_runner import RDFoxRunner

from .datasource import Datasource
from .namespace import PROBS

logger = logging.getLogger(__name__)


NAMESPACES = {
    "sys": Namespace("https://ukfires.org/probs/system/"),
    "": PROBS,
    "rdf": RDF,
    "rdfs": RDFS,
}


def probs_convert_data(datasources, output_path, working_dir=None, script_source_dir=None) -> None:
    """Run RDFox to load `facts` and `rules` then return answer from `queries`.

    :param datasources: list of Datasource
    :param output_path: path to save the data
    :param working_dir: Path to setup rdfox in, defaults to a temporary directory
    :param script_source_dir: Path to copy scripts from
    """

    # Standard files
    FILES = [
        "probs.fss",
        "additional_info.ttl",
        "scripts/conversion/init.rdfox",
        "scripts/conversion/rules.dlog",
        "scripts/conversion/object_composition",
        "scripts/conversion/save_data.rdfox",
    ]

    if script_source_dir is None:
        # Use the version of the ontology scripts bundled with the Python
        # package
        script_source_dir = importlib_resources.files("probs_ontology")

    input_files = {
        path: script_source_dir / path
        for path in FILES
    }

    # Datasources -- the actual info
    input_files["scripts/conversion/load_data.rdfox"] = StringIO(
        "\n".join(source.load_data_script for source in datasources)
    )
    input_files["scripts/conversion/map.dlog"] = StringIO(
        "\n".join(source.rules for source in datasources)
    )
    for datasource in datasources:
        for tgt, src in datasource.input_files.items():
            if tgt in input_files:
                raise ValueError(f"Duplicate entry in input_files for '{tgt}'")
            input_files[tgt] = src

    # Placeholder for data
    input_files["data/.placeholder"] = StringIO("")

    script = [
        # Not reusing conversion/master because it ends with quit
        'exec scripts/conversion/init',

        # Actual data
        'exec load_data',
        'import map.dlog',

        # Rest of conversion step
        'import rules.dlog',
        'exec object_composition/pcsc_algorithm',
        'exec save_data',  # includes some drop/clear steps that are needed?
        'quit',
    ]

    with RDFoxRunner(input_files, script, NAMESPACES, working_dir=working_dir) as rdfox:
        shutil.copy(rdfox.files("data/probs_data.nt.gz"), output_path)


def probs_query_data(
    facts_path, queries, working_dir=None, script_source_dir=None
) -> Dict:
    """Run RDFox to query pre-prepared facts.

    :param facts_path: Path to where facts have been written (in ".nt.gz" format)
    :param queries: Dict of {query_name: query_text}, or list of [query_text].
    :param working_dir: Path to setup rdfox in, defaults to a temporary directory
    :param script_source_dir: Path to copy scripts from
    :return: Dict of {query_name: result}
    """
    if isinstance(queries, list):
        queries = {i: query_text for i, query_text in enumerate(queries)}
    elif not isinstance(queries, dict):
        raise ValueError("query should be list or dict")

    # Standard files
    FILES = [
        "probs.fss",
        "additional_info.ttl",
        "scripts/reasoning/master.rdfox",
        "scripts/reasoning/init.rdfox",
        "scripts/reasoning/load_data.rdfox",
        "scripts/reasoning/rules.dlog",
    ]

    if script_source_dir is None:
        # Use the version of the ontology scripts bundled with the Python
        # package
        script_source_dir = importlib_resources.files("probs_ontology")

    input_files = {
        path: script_source_dir / path
        for path in FILES
    }

    # Add in the actual data
    input_files["data/probs_data.nt.gz"] = facts_path

    script = [
        'dstore create default par-complex-nn',
        'exec scripts/reasoning/init',
        'exec load_data',
        'import rules.dlog',
        'set endpoint.port "12112"',
        'endpoint start',
    ]

    with RDFoxRunner(input_files, script, NAMESPACES, working_dir=working_dir) as rdfox:
        answers_df = {
            query_name: rdfox.query_records(query_text)
            for query_name, query_text in queries.items()
        }

    with pd.option_context('display.max_rows', 100, 'display.max_columns', 10, 'display.max_colwidth', 200):
        for k, v in answers_df.items():
            logger.info("Results from query %s:", k)
            logger.info("\n%s", pd.DataFrame.from_records(v))

    return answers_df


@contextmanager
def probs_endpoint(
    facts_path, working_dir=None, script_source_dir=None
) -> Iterator:
    """Run RDFox to query pre-prepared facts.

    :param facts_path: Path to where facts have been written (in ".nt.gz" format)
    :param working_dir: Path to setup rdfox in, defaults to a temporary directory
    :param script_source_dir: Path to copy scripts from
    :return: Dict of {query_name: result}
    """
    # Standard files
    FILES = [
        "probs.fss",
        "additional_info.ttl",
        "scripts/reasoning/master.rdfox",
        "scripts/reasoning/init.rdfox",
        "scripts/reasoning/load_data.rdfox",
        "scripts/reasoning/rules.dlog",
    ]

    if script_source_dir is None:
        # Use the version of the ontology scripts bundled with the Python
        # package
        script_source_dir = importlib_resources.files("probs_ontology")

    input_files = {
        path: script_source_dir / path
        for path in FILES
    }

    # Add in the actual data
    input_files["data/probs_data.nt.gz"] = facts_path

    script = [
        'dstore create default par-complex-nn',
        'exec scripts/reasoning/init',
        'exec load_data',
        'import rules.dlog',
        'set endpoint.port "12112"',
        'endpoint start',
    ]

    with RDFoxRunner(input_files, script, NAMESPACES, working_dir=working_dir) as rdfox:
        yield rdfox


def answer_queries_with_rdfox(
    datasources, queries, print_facts=False, working_dir=None, script_source_dir=None
) -> Dict:
    """Run RDFox to load `facts` and `rules` then return answer from `queries`.

    :param facts: Facts in ttl format (string)
    :param rules: Facts in datalog format (string)
    :param queries: Dict of {query_name: query_text}, or list of [query_text].
    :param print_facts: whether to dump all RDFox facts for debugging
    :param working_dir: Path to setup rdfox in, defaults to a temporary directory
    :param script_source_dir: Path to copy scripts from
    :return: Dict of {query_name: result}
    """
    if isinstance(queries, list):
        queries = {i: query_text for i, query_text in enumerate(queries)}
    elif not isinstance(queries, dict):
        raise ValueError("query should be list or dict")

    # Standard files
    FILES = [
        "probs.fss",
        "additional_info.ttl",
        "scripts/conversion/init.rdfox",
        "scripts/conversion/rules.dlog",
        "scripts/conversion/object_composition",
        "scripts/conversion/save_data.rdfox",
        "scripts/reasoning/init.rdfox",
        # "scripts/reasoning/load_data.rdfox",
        "scripts/reasoning/rules.dlog",
    ]

    if script_source_dir is None:
        # Use the version of the ontology scripts bundled with the Python
        # package
        script_source_dir = importlib_resources.files("probs_ontology")

    input_files = {
        path: script_source_dir / path
        for path in FILES
    }

    # Datasources -- the actual info
    input_files["scripts/conversion/load_data.rdfox"] = StringIO(
        "\n".join(source.load_data_script for source in datasources)
    )
    input_files["scripts/conversion/map.dlog"] = StringIO(
        "\n".join(source.rules for source in datasources)
    )
    for datasource in datasources:
        for tgt, src in datasource.input_files.items():
            if tgt in input_files:
                raise ValueError(f"Duplicate entry in input_files for '{tgt}'")
            input_files[tgt] = src

    # Placeholder for data
    input_files["data/.placeholder"] = StringIO("")

    script = [
        # Not reusing conversion/master because it ends with quit
        'exec scripts/conversion/init',

        # Actual data
        'exec load_data',
        'import map.dlog',

        # Rest of conversion step
        'import rules.dlog',
        'exec object_composition/pcsc_algorithm',
        'exec save_data',  # includes some drop/clear steps that are needed?

        # Reasoning step
        'exec scripts/reasoning/init',
        'import rules.dlog',

        # Start the endpoint
        'set endpoint.port "12112"',
        'endpoint start',
    ]

    with RDFoxRunner(input_files, script, NAMESPACES, working_dir=working_dir) as rdfox:
        if print_facts:
            print()
            print("--- Dump of RDFox data: ---")
            print(rdfox.facts())

        answers_df = {
            query_name: rdfox.query_records(query_text)
            for query_name, query_text in queries.items()
        }

    with pd.option_context('display.max_rows', 100, 'display.max_columns', 10, 'display.max_colwidth', 200):
        for k, v in answers_df.items():
            logger.info("Results from query %s:", k)
            logger.info("\n%s", pd.DataFrame.from_records(v))

    return answers_df


class ProbsFacts:
    def __init__(self, sources, print_facts=False, working_dir=None, script_source_dir=None):
        if isinstance(sources, str):
            sources = [Datasource.from_facts(sources)]

        self.sources = sources
        self.print_facts = print_facts
        self.working_dir = working_dir
        self.script_source_dir = script_source_dir

    def query(self, query):
        if isinstance(query, str):
            query = [query]
            unwrap = True
        else:
            unwrap = False

        result = answer_queries_with_rdfox(
            self.sources, query, self.print_facts, self.working_dir, self.script_source_dir
        )

        return result[0] if unwrap else result

    def query_one(self, query):
        result = self.query(query)
        if len(result) != 1:
            raise ValueError(f"Expected only 1 result but got {len(result)}")
        return result[0]
