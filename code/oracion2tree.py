"""
oracion2tree.py
Descripción. Se realiza el árbol de derivación de la oración 
"Octavio envió cartas a su amada" usando la librería SpaCy. 
"""

from discopy.grammar.dependency import from_spacy
import spacy 

nlp = spacy.load("es_core_news_sm")
doc = nlp("Octavio envió cartas a su amada")

from_spacy(doc).to_diagram().draw(figsize=(4, 4))