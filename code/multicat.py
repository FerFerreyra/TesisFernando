"""
multicat.py
Descripción. El código define objetos y morfismos en una multicategoría libre
usando DisCoPy. También muestra como obtener diagramas de los morfismos en la multicategoría. 
"""

from discopy.grammar.cfg import Ty, Tree, Rule, Word

x, y = Ty('x'), Ty('y')
f, g, h = Rule(x @ x, x, name='f'), Rule(x @ y, x, name='g'), Rule(y @ x, x, name='h')

f.to_diagram().foliation().draw()

f(g, h).to_diagram().foliation().draw()
