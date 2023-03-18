import os
import sys
from pylode import OntDoc

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSIONS_DIR = os.path.join(ROOT_DIR, "versions")


def main():
    latest_version_dir = sorted(os.listdir(VERSIONS_DIR))[-1]
    version_dirs = [latest_version_dir]

    for version_dir in version_dirs:
        input_file = os.path.join(
            VERSIONS_DIR, version_dir, "concatenated_ontology.ttl")

        # Check if the input file exists
        if not os.path.isfile(input_file):
            print(f"Error: The input file '{input_file}' does not exist.")
            sys.exit(1)

        # Generate documentation for the explicit version
        output_file_explicit = os.path.join(
            VERSIONS_DIR, version_dir, "documentation", "index.html")
        os.makedirs(os.path.dirname(output_file_explicit), exist_ok=True)
        od_explicit = OntDoc(ontology=input_file)
        od_explicit.make_html(destination=output_file_explicit)
        print(f"Generated documentation: {output_file_explicit}")

        # Generate documentation for the latest version
        output_file_latest = os.path.join(
            VERSIONS_DIR, "latest", "documentation", "index.html")
        os.makedirs(os.path.dirname(output_file_latest), exist_ok=True)
        od_latest = OntDoc(ontology=input_file)
        od_latest.make_html(destination=output_file_latest)
        print(f"Generated documentation: {output_file_latest}")


if __name__ == "__main__":
    main()
