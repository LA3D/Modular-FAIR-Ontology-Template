# Modular Ontology Template

This template provides a structured approach for building and maintaining modular ontologies that follow the FAIR Guidelines for Ontologies and Vocabularies. It uses a GitHub-based repository structure to store and manage ontology modules, design patterns, versioning, competency questions, provenance logs, and documentation.

## Repository Structure

The repository is organized into the following folders and files:

- `modules/`: Contains individual ontology modules (e.g., `common_metadata.ttl`, `module1.ttl`, `module2.ttl`)
- `patterns/`: Contains ontology design patterns (e.g., `pattern1.ttl`, `pattern2.ttl`)
- `versions/`: Contains different versions of the concatenated ontology in various formats (e.g., `.ttl`, `.owl`, `.jsonld`)
- `competency_questions/`: Contains SPARQL queries for competency questions (e.g., `question1.rq`, `question2.rq`)
- `provenance_logs/`: Contains provenance logs for ChatGPT modeling sessions (e.g., `chatgpt_log1.ttl`, `chatgpt_log2.ttl`)
- `documentation/`: Contains human-readable documentation generated from the ontology (e.g., `index.html`, `ontology_description.md`)
- `scripts/`: Contains Python scripts and shell scripts for ontology processing (e.g., `concatenate_modules.py`, `generate_shacl_and_jsonld.py`, `test_competency_questions.py`, `local_testing.sh`)
- `.github/workflows/`: Contains GitHub Actions workflows for automating ontology processing tasks (e.g., `ontology_processing.yml`)
- `.htaccess`: Configuration file for content negotiation and redirection using w3id.org namespaces
- `README.md`: This README file

## Getting Started

1. Clone or download this template repository.
2. Modify the ontology modules and patterns in the `modules/` and `patterns/` folders according to your domain requirements.
3. Update the `.htaccess` file with the appropriate content negotiation and redirection rules for your ontology namespace.
4. Configure the scripts in the `scripts/` folder to match your repository structure and ontology requirements.
5. Define competency questions and their corresponding SPARQL queries in the `competency_questions/` folder.
6. Store logs of ChatGPT modeling sessions as provenance in the `provenance_logs/` folder.
7. Use the provided GitHub Actions workflow to automate the concatenation, validation, and documentation generation processes.

For local testing and development, use the `local_testing.sh` script to set up the environment and execute the Python scripts for concatenating modules, generating SHACL shapes and JSON-LD contexts, and testing competency questions.

## Contributing

To contribute to this template, please submit a pull request with your proposed changes, bug fixes, or enhancements.

## Using ChatGPT for Ontology Modeling

ChatGPT is a powerful AI language model that can assist you in various ontology modeling tasks, such as background conceptualization, modular ontology development, and knowledge graph construction. By priming ChatGPT with appropriate context and goals, you can receive valuable guidance and insights for your ontology projects.

To effectively use ChatGPT as an ontology modeling assistant:

1. **Set the context**: Use concise prompts to provide a clear context for the modeling task. Include details about the ontology's structure, domain, and goals. For example, mention the FAIR guidelines, modular organization, and knowledge graph construction.

2. **Ask for specific guidance**: Request help with specific tasks, such as defining classes, properties, or instances, using ontology design patterns, or integrating data sources with RDF Mapping Language (RML).

3. **Collaborate on competency questions**: Work with ChatGPT to define and refine competency questions for your ontology. These questions can help you assess the ontology's ability to answer relevant queries and guide its development.

4. **Maintain context across sessions**: To ensure continuity and context preservation across multiple chat sessions, start each new session by summarizing the outcomes and insights from previous sessions. This will help ChatGPT provide consistent and relevant assistance.

5. **Iteratively refine your ontology**: Use ChatGPT to iteratively refine your ontology, addressing potential issues, inconsistencies, or gaps in the model. This will help you create a more robust and well-structured ontology that adheres to best practices.

By following these guidelines and using ChatGPT as a collaborative ontology modeling assistant, you can accelerate the development process and create ontologies that are more findable, accessible, interoperable, and reusable.
W

## ChatGPT Prompt Priming

To prime ChatGPT for ontology modeling assistance, use the following prompts:

- Concise summary prompt:

> You are ChatGPT, an AI language model, and you are assisting with the development of a modular ontology that follows FAIR guidelines for ontologies and vocabularies. The ontology is being built using a GitHub repository structure that contains modules, design patterns, versioning, competency questions, provenance logs, and documentation. The project aims to facilitate interoperability using web standard ontologies and crosswalks. The goal is to create a structured and maintainable ontology that can be easily used, understood, and extended.

- Repository structure and scripts prompt:

> You are ChatGPT, an AI language model, and you are assisting with the development of a modular ontology that follows FAIR guidelines for ontologies and vocabularies. The project uses a GitHub repository structure with modules, patterns, versions, competency questions, provenance logs, and documentation. The repository includes Python scripts (`concatenate_modules.py`, `generate_shacl_and_jsonld.py`, and `test_competency_questions.py`) and a shell script (`local_testing.sh`) for processing the ontology. It also uses a `.htaccess` file for content negotiation and redirection using w3id.org namespaces. You understand how the repository is organized and how the scripts and workflows function in order to provide effective assistance in ontology modeling tasks.

- Knowledge Graph Construction

> You are ChatGPT, an AI language model, and you are assisting with the construction of a Knowledge Graph using a modular ontology developed following the FAIR guidelines. The ontology is organized into modules, patterns, and versions, and it is designed for a specific domain (e.g., books). Your task is to provide guidance on creating a Knowledge Graph that adheres to the ontology's structure, including the use of classes, properties, and instances. You should also help with mapping between various data sources and the ontology using technologies such as RDF Mapping Language (RML) to ensure seamless integration. Additionally, provide support in the application of best practices for RDF data representation and querying, such as using SPARQL and JSON-LD. Your goal is to make the constructed Knowledge Graph findable, accessible, interoperable, and reusable.

---

## Helpful References

1.  [FAIR Principles](https://www.go-fair.org/fair-principles/)

    - A detailed explanation of the FAIR principles for making data findable, accessible, interoperable, and reusable.

2.  [OWL 2 Web Ontology Language Primer](https://www.w3.org/TR/owl2-primer/)

    - A gentle introduction to the OWL 2 Web Ontology Language for those who are new to ontology modeling.

3.  [Turtle - Terse RDF Triple Language](https://www.w3.org/TR/turtle/)

    - The official W3C recommendation on the Turtle syntax for expressing RDF graphs in a concise and readable way.

4.  [SHACL - Shapes Constraint Language](https://www.w3.org/TR/shacl/)

    - The W3C recommendation on SHACL, a language for validating RDF graphs against a set of conditions.

5.  [JSON-LD - JSON for Linking Data](https://www.w3.org/TR/json-ld/)

    - The W3C recommendation on JSON-LD, a lightweight Linked Data format for expressing RDF data in JSON.

6.  [PySHACL](https://github.com/RDFLib/pySHACL)

    - The official GitHub repository of the PySHACL library, a Python validator for SHACL.

7.  [Widoco - A tool to generate ontology documentation](https://github.com/dgarijo/Widoco)

    - The official GitHub repository of Widoco, a tool to generate human-readable documentation for ontologies.

8.  [PyLODE - A Python tool for generating Linked Data documentation](https://github.com/rdflib/pyLODE)

    - The official GitHub repository of PyLODE, a Python library to generate human-readable Linked Data documentation.

9.  [WebVOWL - Web-based Visualization of Ontologies](http://vowl.visualdataweb.org/webvowl.html)

    - A web-based tool for visualizing ontologies in an interactive, graph-based format.

10. [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/)

    - The W3C recommendation on the SPARQL 1.1 Query Language for querying RDF data.

11. [Best Practices for Implementing FAIR Vocabularies and Ontologies on the Web](https://arxiv.org/abs/2003.13084)

    - A research paper discussing the principles for FAIR vocabulary publishing, which can be applied to ontology development.

12. [Ontology Design Patterns](http://ontologydesignpatterns.org/wiki/Main_Page)

    - A collaborative portal containing ontology design patterns that promote modular ontology development and reusability.

13. [NeOn Methodology in a Nutshell](http://neon-project.org/nw/NeOn_Book.html)

    - A comprehensive methodology for ontology engineering, emphasizing modularity and reusability.

14. [Modular Ontology Modeling: Patterns, Challenges and Techniques](https://www.semantic-web-journal.net/content/modular-ontology-modeling-1)

    - A research paper discussing the challenges and techniques for modular ontology modeling.

15. [Good Ontology Design](https://www.w3.org/2001/sw/BestPractices/OEP/)

    - W3C's Semantic Web Best Practices and Deployment Working Group page on ontology engineering practices.

16. [OPLaX: annotating ontology design patterns at
    conceptual and instance level](https://ceur-ws.org/Vol-3011/paper1.pdf)

        - Annotations to create and implement FAIR ontology design patterns.
