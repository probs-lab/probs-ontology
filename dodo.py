def task_ontology_conversion():
    """Converts the Turtle ontology into Datalog rules, and data."""
    return {
        'file_dep': [
            'ontology/probs.ttl',
        ],
        'targets': [
            'data/probs_ontology_data.nt.gz',
            'data/probs_ontology_rules.dlog',
        ],
        'actions': [
            convert_ontology
        ],
    }


def convert_ontology():
    from probs_runner import probs_convert_ontology
    from pathlib import Path
    import logging
    logging.basicConfig(level=logging.DEBUG)
    output_dir = Path("data")
    output_dir.mkdir(exist_ok=True, parents=True)
    probs_convert_ontology(
        "ontology/probs.ttl",
        additional_data=[
            "ontology/prov-o.ttl",
            "ontology/qudt.ttl",
            "ontology/qudt_quantitykind.ttl",
            "ontology/qudt_unit.ttl",
            "ontology/time.ttl",
            "ontology/UK.ttl",
            "ontology/probs.ttl",
            "ontology/time_periods.ttl",
        ],
        output_dir="data",
        working_dir="working",
    )
