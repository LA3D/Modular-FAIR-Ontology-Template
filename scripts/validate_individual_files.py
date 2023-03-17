from rdflib import Graph
import sys
import os


def validate_turtle_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.ttl'):
                file_path = os.path.join(root, file)
                try:
                    g = Graph()
                    g.parse(file_path, format='turtle')
                    print(f"Successfully validated: {file_path}")
                except Exception as e:
                    print(f"Error validating: {file_path}\nError: {e}")


def main():
    script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    root_dir = os.path.dirname(script_dir)

    # Validate modules and patterns
    validate_turtle_files(os.path.join(root_dir, 'modules'))
    validate_turtle_files(os.path.join(root_dir, 'patterns'))


if __name__ == "__main__":
    main()
