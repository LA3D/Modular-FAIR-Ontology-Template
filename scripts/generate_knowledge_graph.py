import os
import rdflib
from rdflib.namespace import RDF, OWL, RDFS, Namespace
from rdflib.plugins.sparql import prepareQuery
from rdflib.plugins.sparql.processor import SPARQLResult

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def apply_reasoning(graph):
    """
    Apply OWL reasoning to the input graph and return a new graph
    """
    new_graph = rdflib.Graph()
    new_graph += graph  # Create a new graph with the original data

    # Use the OWL RL semantics to apply RDFS and OWL reasoning
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(new_graph)

    return new_graph


def serialize_knowledge_graph(graph, output_file):
    """
    Serialize the RDFLib Graph object to a file
    """
    ns = Namespace('https://w3id.org/your-ontology-uri#')

    # Bind the namespace to the prefix
    graph.bind('your-prefix', ns)

    # Serialize the graph to the output file
    with open(output_file, 'w') as f:
        f.write(graph.serialize(format='turtle'))

    print(f"Knowledge graph saved to: {output_file}")


def main():
    # Define input directories and output file
    modules_dir = os.path.join(ROOT_DIR, 'modules')
    patterns_dir = os.path.join(ROOT_DIR, 'patterns')
    instances_dir = os.path.join(ROOT_DIR, 'instances')
    kg_dir = os.path.join(ROOT_DIR, 'knowledge_graphs')
    output_file = os.path.join(kg_dir, 'sample_knowledge_graph.ttl')

    # Create the RDFLib Graph
    graph = rdflib.Graph()

    # Load ontology modules
    for file_name in os.listdir(modules_dir):
        file_path = os.path.join(modules_dir, file_name)
        graph.parse(file_path, format='turtle')

    # Load ontology patterns
    for file_name in os.listdir(patterns_dir):
        file_path = os.path.join(patterns_dir, file_name)
        graph.parse(file_path, format='turtle')

    # Load instance data
    for file_name in os.listdir(instances_dir):
        file_path = os.path.join(instances_dir, file_name)
        graph.parse(file_path, format='turtle')

    # Apply reasoning
    graph = apply_reasoning(graph)

    # Serialize the knowledge graph
    serialize_knowledge_graph(graph, output_file)


if __name__ == '__main__':
    # Import owlrl after __name__ check to avoid NameError
    import owlrl
    main()
