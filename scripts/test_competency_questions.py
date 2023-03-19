import re
import os
import sys
import ast
from rdflib import Graph, URIRef
from rdflib.plugins.sparql import prepareQuery

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPETENCY_QUESTIONS_DIR = os.path.join(ROOT_DIR, "competency_questions")
CONCATENATED_ONTOLOGY_PATH = os.path.join(
    ROOT_DIR, "versions", "latest", "concatenated_ontology.ttl")


def extract_expected_results(content: str):
    match = re.search(
        r"# Expected results \(as a Python list of tuples\):\n(.*?)\n\n", content, re.DOTALL)
    if match:
        print("Matched content:")
        print(match.group(1))

        cleaned_content = re.sub(r'\s*#.*', '', match.group(1))
        print("Cleaned content:")
        print(cleaned_content)

        try:
            expected_results = ast.literal_eval(cleaned_content)
            return expected_results
        except SyntaxError as e:
            print(f"Syntax error while parsing expected results: {e}")
            return None
    else:
        print("No expected results found")
        return None


def main():
    # Load the concatenated ontology
    g = Graph()
    g.parse(CONCATENATED_ONTOLOGY_PATH, format="turtle")
    print(g.serialize(format="turtle"))

    # Iterate through the competency questions directory and find all .rq files
    for file_name in os.listdir(COMPETENCY_QUESTIONS_DIR):
        if file_name.endswith(".rq"):
            file_path = os.path.join(COMPETENCY_QUESTIONS_DIR, file_name)

            # Read the SPARQL query content
            with open(file_path, "r") as f:
                query_content = f.read()

            print(f"Processing query file: {file_name}")
            print("Query content:")
            print(query_content)

            # Extract the expected results
            expected_results = extract_expected_results(query_content)

            # Prepare and execute the query
            query = prepareQuery(query_content)
            results = g.query(query)
            actual_results = [tuple(str(x) for x in row) for row in results]

            # Compare the actual results with the expected results
            if expected_results is None:
                print(f"No expected results found for {file_name}")
            elif expected_results == actual_results:
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
