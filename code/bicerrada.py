"""
bicerrada.py
Descripción. El código define objetos y morfismos en una categoría bicerrada libre
usando DisCoPy. También muestra como se realiza el curry y uncurry.
"""
from discopy.closed import Ty, Box, Curry

x, y, z = map(Ty, "xyz")
f, g, h = Box('f', x, z << y), Box('g', x @ y, z), Box('h', y, x >> z)

f.uncurry()
g.curry()
h.uncurry(left=False)