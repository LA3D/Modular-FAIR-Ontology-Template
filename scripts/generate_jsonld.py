import os
import json
from rdflib import Graph, Namespace, plugin
from rdflib.serializer import Serializer


def generate_jsonld(root_dir):
    # Set up namespace prefixes
    init_ns = {
        "owl": Namespace("http://www.w3.org/2002/07/owl#"),
        "rdf": Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
        "rdfs": Namespace("http://www.w3.org/2000/01/rdf-schema#"),
        "xsd": Namespace("http://www.w3.org/2001/XMLSchema#"),
        "xml": Namespace("http://www.w3.org/XML/1998/namespace"),
        "dct": Namespace("http://purl.org/dc/terms/"),
        "foaf": Namespace("http://xmlns.com/foaf/0.1/"),
        "oplax": Namespace("http://www.ontologydesignpatterns.org/oplax/"),
        "oplax1": Namespace("https://w3id.org/OPLaX/"),
        "skos": Namespace("http://www.w3.org/2004/02/skos/core#"),
        "vann": Namespace("http://purl.org/vocab/vann/"),
        "void": Namespace("http://rdfs.org/ns/void#"),
        "your-prefix": Namespace("https://w3id.org/your-ontology-uri/"),
    }

    # Create an empty RDF graph
    g = Graph()

    # Bind the namespace prefixes to the graph
    for prefix, uri in init_ns.items():
        g.bind(prefix, uri)

    # Load all TTL files in the 'modules' directory
    modules_dir = os.path.join(root_dir, "modules")
    for filename in os.listdir(modules_dir):
        if filename.endswith(".ttl"):
            module_path = os.path.join(modules_dir, filename)
            g.parse(module_path, format="turtle")

    # Load all TTL files in the 'patterns' directory
    patterns_dir = os.path.join(root_dir, "patterns")
    for filename in os.listdir(patterns_dir):
        if filename.endswith(".ttl"):
            pattern_path = os.path.join(patterns_dir, filename)
            g.parse(pattern_path, format="turtle")

    # Serialize the graph to JSON-LD
    json_ld = g.serialize(format="json-ld", indent=4)

    # Write the JSON-LD to file
    json_ld_path = os.path.join(
        root_dir, "versions", "latest", "ontology.jsonld")
    with open(json_ld_path, "w") as f:
        f.write(json_ld)

    print(f"Generated {json_ld_path}")


if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    generate_jsonld(root_dir)
