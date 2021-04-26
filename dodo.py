
# change this if RDFox is not in your path
rdfox_path = "RDFox"


def task_ontology2fss():
    """Converts the Turtle ontology into Functional-Style OWL."""
    return {
        'file_dep': [
            'probs_ontology/probs.ttl',
            'probs_ontology/scripts/ontology2ffs/master.rdfox',
            'probs_ontology/scripts/ontology2ffs/init.rdfox',
            'probs_ontology/scripts/ontology2ffs/convert.rdfox',
        ],
        'targets': [
            'probs_ontology/probs.fss',
        ],
        'actions': [
            f'{rdfox_path} sandbox probs_ontology "exec scripts/ontology2ffs/master"'
        ],
    }
