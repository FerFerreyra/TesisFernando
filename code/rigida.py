"""
rigida.py
Descripción. Define las evaluaciones y coevaluaciones izquierdas y derechas
para un objeto en una categoría rígida. 
"""
from discopy.grammar.pregroup import Ty, Cup, Cap

n = Ty('n')
Cap(n.l,n)
Cap(n,n.r)
Cup(n,n.l)
Cup(n.r,n)