import pyshacl
import rdflib

# Define the FAIR SHACL shapes
fair_shapes = """
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix fair: <http://example.com/fair-shapes#> .

# Shape for classes
fair:ClassShape
  a sh:NodeShape ;
  sh:targetClass rdfs:Class ;
  sh:property [
    sh:path rdfs:label ;
    sh:minCount 1 ;
    sh:severity sh:Violation ;
    sh:message "rdfs:Class must have a label." ;
  ] ;
  sh:property [
    sh:path rdfs:comment ;
    sh:minCount 1 ;
    sh:severity sh:Violation ;
    sh:message "rdfs:Class must have a comment." ;
  ] .

# Shape for properties
fair:PropertyShape
  a sh:NodeShape ;
  sh:targetClass rdf:Property ;
  sh:property [
    sh:path rdfs:label ;
    sh:minCount 1 ;
    sh:severity sh:Violation ;
    sh:message "rdf:Property must have a label." ;
  ] ;
  sh:property [
    sh:path rdfs:comment ;
    sh:minCount 1 ;
    sh:severity sh:Violation ;
    sh:message "rdf:Property must have a comment." ;
  ] .

# Shape for the ontology
fair:OntologyShape
  a sh:NodeShape ;
  sh:targetSubjectsOf rdf:type ;
  sh:property [
    sh:path rdfs:label ;
    sh:minCount 1 ;
    sh:severity sh:Violation ;
    sh:message "Ontology must have a label." ;
  ] ;
  sh:property [
    sh:path rdfs:comment ;
    sh:minCount 1 ;
    sh:severity sh:Violation ;
    sh:message "Ontology must have a comment." ;
  ] ;
  sh:property [
    sh:path <http://purl.org/dc/terms/creator> ;
    sh:minCount 1 ;
    sh:severity sh:Violation ;
    sh:message "Ontology must have a creator." ;
  ] ;
  sh:property [
    sh:path <http://purl.org/dc/terms/created> ;
    sh:minCount 1 ;
    sh:severity sh:Violation ;
    sh:message "Ontology must have a creation date." ;
  ] ;
  sh:property [
    sh:path <http://purl.org/dc/terms/license> ;
    sh:minCount 1 ;
    sh:severity sh:Violation ;
    sh:message "Ontology must have a license." ;
  ] .
"""

# Load the concatenated ontology file
g = rdflib.Graph()
g.parse("versions/latest/concatenated_ontology.ttl", format="turtle")

# Load the FAIR SHACL shapes
shapes_graph = rdflib.Graph()
shapes_graph.parse(data=fair_shapes, format="turtle")

# Validate the ontology against the FAIR SHACL shapes
r = pyshacl.validate(g, shacl_graph=shapes_graph, ont_graph_format="turtle",
                     shacl_graph_format="turtle", inference="none")

# Print validation results
conforms, results_graph, results_text = r
if conforms:
    print("Ontology conforms to FAIR SHACL shapes!")
else:
    print(results_text)
