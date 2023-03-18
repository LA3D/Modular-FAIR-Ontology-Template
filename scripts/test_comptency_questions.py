import os
import sys
from rdflib import Graph, URIRef
from rdflib.plugins.sparql import prepareQuery

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPETENCY_QUESTIONS_DIR = os.path.join(ROOT_DIR, "competency_questions")
CONCATENATED_ONTOLOGY_PATH = os.path.join(
    ROOT_DIR, "versions", "latest", "concatenated_ontology.ttl")


def extract_expected_results(content):
    start = content.find("# Expected results")
    if start == -1:
        return None

    content = content[start:]
    end = content.find("#")
    if end != -1:
        content = content[:end]

    return eval(content.split(":", 1)[-1].strip())


def main():
    # Load the concatenated ontology
    g = Graph()
    g.parse(CONCATENATED_ONTOLOGY_PATH, format="turtle")

    # Iterate through the competency questions directory and find all .rq files
    for file_name in os.listdir(COMPETENCY_QUESTIONS_DIR):
        if file_name.endswith(".rq"):
            file_path = os.path.join(COMPETENCY_QUESTIONS_DIR, file_name)

            # Read the SPARQL query content
            with open(file_path, "r") as f:
                query_content = f.read()

            # Extract the expected results
            expected_results = extract_expected_results(query_content)

            # Prepare and execute the query
            query = prepareQuery(query_content)
            results = g.query(query)
            actual_results = [tuple(str(x) for x in row) for row in results]

            # Compare the actual results with the expected results
            if expected_results == actual_results:
                print(f"Test passed for {file_name}")
            else:
                print(f"Test failed for {file_name}")
                print("Expected results:")
                print(expected_results)
                print("Actual results:")
                print(actual_results)

            print("\n")


if __name__ == "__main__":
    main()
