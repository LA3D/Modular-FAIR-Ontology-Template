import os
import rdflib
from rdflib.namespace import OWL

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_ontology_version(graph):
    ontology_uri = list(graph.subjects(
        predicate=rdflib.RDF.type, object=OWL.Ontology))[0]
    version_info = graph.value(subject=ontology_uri, predicate=OWL.versionInfo)
    return str(version_info)


def main():
    # Define input directories and output file
    modules_dir = os.path.join(ROOT_DIR, "modules")
    patterns_dir = os.path.join(ROOT_DIR, "patterns")

    # Create the RDFLib Graph
    g = rdflib.Graph()

    # Load ontology modules
    for file_name in os.listdir(modules_dir):
        file_path = os.path.join(modules_dir, file_name)
        g.parse(file_path, format="turtle")

    # Load ontology patterns
    for file_name in os.listdir(patterns_dir):
        file_path = os.path.join(patterns_dir, file_name)
        g.parse(file_path, format="turtle")

    # Get the ontology version from the common_metadata.ttl
    version = get_ontology_version(g)

    # Create the version directory if it doesn't exist
    version_dir = os.path.join(ROOT_DIR, "versions", version)
    os.makedirs(version_dir, exist_ok=True)

    # Serialize the concatenated ontology to the output file
    output_file = os.path.join(version_dir, "concatenated_ontology.ttl")
    with open(output_file, "w") as f:
        f.write(g.serialize(format="turtle"))

    print(f"Concatenated ontology saved to: {output_file}")

    # Save the latest version
    latest_dir = os.path.join(ROOT_DIR, "versions", "latest")
    os.makedirs(latest_dir, exist_ok=True)
    latest_output_file = os.path.join(latest_dir, "concatenated_ontology.ttl")
    with open(latest_output_file, "w") as f:
        f.write(g.serialize(format="turtle"))

    print(f"Latest concatenated ontology saved to: {latest_output_file}")


if __name__ == "__main__":
    main()
