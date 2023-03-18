import os
import sys
import argparse
from rdflib import Graph, RDF
from rdflib.namespace import OWL, RDFS, XSD

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(ROOT_DIR, "modules")
PATTERNS_DIR = os.path.join(ROOT_DIR, "patterns")


def validate_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".ttl"):
                filepath = os.path.join(root, file)
                validate_file(filepath)


def validate_file(filepath):
    print(f"Validating: {filepath}")
    g = Graph()
    try:
        g.parse(filepath, format="turtle")
    except Exception as e:
        print(f"Error validating: {filepath}")
        print(f"Error: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Validate Turtle files in modules and patterns directories.")
    parser.add_argument(
        "--input_file", help="Specify a single Turtle file to validate")
    args = parser.parse_args()

    if args.input_file:
        validate_file(args.input_file)
    else:
        validate_files(MODULES_DIR)
        validate_files(PATTERNS_DIR)


if __name__ == "__main__":
    main()
