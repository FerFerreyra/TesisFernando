"""
monoidal.py
Descripción. El código define objetos y morfismos en una categoría monoidal libre
usando DisCoPy. También muestra como obtener diagramas de los morfismos en la categoría. 
"""

from discopy.monoidal import Ty, Box, Diagram
from discopy.drawing import Equation

x = Ty("x")
y, z, w = Ty(*"yzw")

f, g, h = Box('f', x, y), Box('g', z, w), Box('h', y, z)

(f.then(h)).draw(figsize=(2, 2))
(f @ g).draw(figsize=(2, 2))
(f.then(h) @ g).draw(figsize=(5, 5)) 

Equation(
    (f @ g).interchange(0, 1), (f @ g),
    symbol="$=$").draw(figsize=(5, 2))