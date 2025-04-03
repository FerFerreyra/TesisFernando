"""
cat.py
Descripción. El código define objetos y morfismos en una categoría libre
usando DisCoPy.
"""

from discopy.cat import Ob, Box
    
w, x, y, z = map(Ob, "wxyz")
h, f, g = Box('h', w, x), Box('f', x, y), Box('g', y, z)

print(type(w))

print(type(f))

print(f)

print(f.then(g))

print(h.then(f).then(g))