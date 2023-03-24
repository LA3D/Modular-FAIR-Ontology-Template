import os
import rdflib
from rdflib import Graph, URIRef, Namespace
from rdflib.plugins.sparql import prepareQuery
from rdflib.plugins.stores.sparqlstore import SPARQLStore

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_ontology_and_instances():
    """
    Loads the concatenated ontology and example instance data into an RDFLib graph.

    Returns:
        A Graph object containing the concatenated ontology and instance data.
    """
    # Define the input file paths
    ontology_path = os.path.join(
        ROOT_DIR, "versions", "latest", "concatenated_ontology.ttl")
    instances_path = os.path.join(
        ROOT_DIR, "instances", "example_instance.ttl")

    # Create an RDFLib graph and load the concatenated ontology and instance data
    graph = Graph()
    graph.parse(ontology_path, format="turtle")
    graph.parse(instances_path, format="turtle")

    return graph


def apply_reasoning(graph):
    """
    Applies OWLRL reasoning to the RDFLib graph.

    Args:
        graph: A Graph object containing the concatenated ontology and instance data.

    Returns:
        A Graph object containing the inferred knowledge graph after reasoning has been applied.
    """
    # Create a new RDFLib graph and load the concatenated ontology and instance data
    new_graph = Graph()
    new_graph.parse(data=graph.serialize(format='turtle'), format='turtle')

    # Apply OWLRL reasoning to the graph
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(new_graph)

    return new_graph


def serialize_knowledge_graph(graph, output_file):
    """
    Serializes the knowledge graph to the output file in Turtle format.

    Args:
        graph: A Graph object containing the inferred knowledge graph after reasoning has been applied.
        output_file: The path to the output file for the serialized knowledge graph.
    """
    # Create a new RDFLib graph to hold the post-reasoning statements
    new_graph = Graph()

    # Define the namespaces for the output graph
    ns = Namespace('https://w3id.org/your-ontology-uri/')
    ns.bind('your-prefix', ns)

    # Define the SPARQL query to retrieve the relevant statements from the post-reasoning graph
    query = prepareQuery(
        """
        SELECT ?s ?p ?o WHERE {
            ?s ?p ?o .
            FILTER(isURI(?s) && isURI(?o))
        }
        """,
        initNs={"ns": ns}
    )

    # Execute the SPARQL query on the post-reasoning graph and add the results to the new graph
    for row in graph.query(query):
        new_graph.add((row[0], row[1], row[2]))

    # Serialize the new graph to the output file in Turtle format
    with open(output_file, "w") as f:
        f.write(new_graph.serialize(format="turtle").decode())

    print(f"Knowledge graph saved to: {output_file}")


def main():
    # Define the input and output file paths
    output_file = os.path.join(
        ROOT_DIR, "knowledge_graphs", "sample_knowledge_graph.ttl")

    # Load the concatenated ontology and instance data
    graph = load_ontology_and_instances()

    # Apply OWLRL reasoning to the graph
    graph = apply_reasoning(graph)

    # Serialize the inferred knowledge graph to the output file
    serialize_knowledge_graph(graph, output_file)


if __name__ == "__main__":
    main()
