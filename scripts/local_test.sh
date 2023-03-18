#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ROOT_DIR=$(dirname "$SCRIPT_DIR")
VENV_PYTHON="$ROOT_DIR/venv/bin/python"

echo "Step 1: Validate individual Turtle files (modules and patterns)"
"$VENV_PYTHON" "$SCRIPT_DIR/validate_individual_files.py"

echo "Step 2: Concatenate the ontology"
"$VENV_PYTHON" "$SCRIPT_DIR/concatenate_ontology.py"

echo "Step 3: Validate the concatenated ontology"
"$VENV_PYTHON" "$SCRIPT_DIR/validate_individual_files.py" --input_file "$ROOT_DIR/versions/latest/concatenated_ontology.ttl"

echo "Step 4: Validate the concatenated ontology against FAIR SHACL shapes"
"$VENV_PYTHON" "$SCRIPT_DIR/validate_ontology.py"

echo "Step 5: Generate documentation"
"$VENV_PYTHON" "$SCRIPT_DIR/generate_documentation.py"

echo "Step 6: Generate JSON-LD"
"$VENV_PYTHON" "$SCRIPT_DIR/generate_jsonld.py"

echo "Step 7: Test competency questions"
"$VENV_PYTHON" "$SCRIPT_DIR/test_competency_questions.py"

echo "Completed local test"