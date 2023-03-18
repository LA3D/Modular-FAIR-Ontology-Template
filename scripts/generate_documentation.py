import os
import sys
from rdflib import Graph, RDF, OWL, RDFS, Namespace
from pylode import OntDoc

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSIONS_DIR = os.path.join(ROOT_DIR, "versions")
CONCATENATED_ONTOLOGY_FILE = os.path.join(
    VERSIONS_DIR, "latest", "concatenated_ontology.ttl")
LATEST_DOCUMENTATION_DIR = os.path.join(
    VERSIONS_DIR, "latest", "documentation")


def main():
    # Load version from concatenated_ontology.ttl
    g = Graph()
    g.parse(CONCATENATED_ONTOLOGY_FILE, format="turtle")
    ontology_uri = list(g.subjects(RDF.type, OWL.Ontology))[0]
    version = str(g.value(subject=ontology_uri, predicate=OWL.versionInfo))

    explicit_version_dir = os.path.join(VERSIONS_DIR, version)
    os.makedirs(explicit_version_dir, exist_ok=True)
    explicit_documentation_dir = os.path.join(
        explicit_version_dir, "documentation")
    os.makedirs(explicit_documentation_dir, exist_ok=True)

    # Generate explicit version documentation
    od = OntDoc(ontology=CONCATENATED_ONTOLOGY_FILE)
    od.make_html(destination=os.path.join(
        explicit_documentation_dir, "index.html"))
    print(
        f"Generated explicit documentation: {os.path.join(explicit_documentation_dir, 'index.html')}")

    # Generate latest documentation
    os.makedirs(LATEST_DOCUMENTATION_DIR, exist_ok=True)
    od.make_html(destination=os.path.join(
        LATEST_DOCUMENTATION_DIR, "index.html"))
    print(
        f"Generated latest documentation: {os.path.join(LATEST_DOCUMENTATION_DIR, 'index.html')}")


if __name__ == "__main__":
    main()
