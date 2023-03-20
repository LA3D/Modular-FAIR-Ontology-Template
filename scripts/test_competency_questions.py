import json
import unittest
from pathlib import Path
from rdflib import Graph
from rdflib.plugins.sparql.processor import prepareQuery

ROOT_DIR = Path(__file__).resolve().parent.parent
COMPETENCY_QUESTIONS_DIR = ROOT_DIR / "competency_questions"
CONCATENATED_ONTOLOGY_PATH = ROOT_DIR / "versions" / \
    "latest" / "concatenated_ontology.ttl"


class TestCompetencyQuestions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load concatenated ontology
        cls.g = Graph()
        cls.g.parse(str(CONCATENATED_ONTOLOGY_PATH), format="turtle")

    def test_competency_question(self):
        for question_file in COMPETENCY_QUESTIONS_DIR.glob("*.jsonld"):
            with self.subTest(question_file=question_file):
                with open(question_file, "r") as f:
                    question_data = json.load(f)

                query = prepareQuery(question_data["query"])
                results = self.g.query(query)

                obtained_results = [str(row[0]) for row in results]
                expected_results = question_data["expected_output"]

                self.assertListEqual(obtained_results, expected_results)


if __name__ == "__main__":
    unittest.main()
