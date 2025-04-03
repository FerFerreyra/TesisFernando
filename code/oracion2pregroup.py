"""
oracion2pregroup.py
Descripción. Implementa la función curry en categorías rígidas. 
Genera la derivación en una gramáticas de pregrupos de la oración
"Octavio envió una carta a su amada"
"""

from discopy.grammar.pregroup import Ty, Id, Box, Diagram
import spacy

def curry(diagram, n_wires=1, left=False):
  if not n_wires > 0:
    return diagram
  if left: #El curry se realiza por la izquierda
    wires = diagram.dom[:n_wires]
    #Sustituimos los primeros cables por sus caps para realizar el curry
    return Diagram.caps(wires.r, wires) @ Id(diagram.dom[n_wires:]) >> Id(wires.r) @ diagram
  wires = diagram.dom[-n_wires:]
  #Sustituimos los ultimos cables por sus caps para realizar el curry
  return Id(diagram.dom[:-n_wires]) @ Diagram.caps(wires, wires.l) >> diagram @ Id(wires.l)
  
def find_root(doc):
    for token in doc:
        if token.dep_ == 'ROOT':
            return token

def doc2rigid(word):
  children = word.children
  #Si la raíz no tiene hijos, terminamos
  if not children:
    return Box(word.text, Ty(word.dep_), Ty())
  #Generamos los objetos por los hijos a la izq y a la derecha
  #y obtenemos la clasificación sintáctica de la palabra en la oración.
  left = Ty(*[child.dep_ for child in word.lefts])
  right = Ty(*[child.dep_ for child in word.rights])
  #Definimos el generador obtenido con la palabra actual
  box = Box(word.text, left.l @ Ty(word.dep_) @ right.r, Ty(),
  data=[left, Ty(word.dep_), right])
  top = curry(curry(box, n_wires=len(left), left=True), n_wires=len(right))
  #Realizamos la llamada recursiva para seguir explorando la oración. 
  bot = Id(Ty()).tensor(*[doc2rigid(child) for child in children])
  return top >> bot

def doc2pregroup(doc):
  root = find_root(doc)
  return doc2rigid(root)

nlp = spacy.load("es_core_news_sm")
doc = nlp("Octavio envió una carta a su amada")

doc2pregroup(doc).draw()