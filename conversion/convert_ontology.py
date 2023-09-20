"""Run the ontology conversion module.

Usage: python convert_ontology.py [PATH TO ADDITIONAL DATA]

Writes to the `data` subdirectory in the same directory as this script.
"""

import sys
from probs_runner import probs_convert_ontology
from pathlib import Path
import logging

logging.basicConfig(level=logging.DEBUG)


def main(paths):
    here = Path(__file__).parent

    output_dir = here / "data"
    output_dir.mkdir(exist_ok=True, parents=True)

    ontology_path = here / "../ontology/probs.ttl"

    probs_convert_ontology(
        ontology_path,
        additional_data=paths,
        output_dir=output_dir,
    )


if __name__ == "__main__":
    main(sys.argv[1:])
    sys.exit(0)
