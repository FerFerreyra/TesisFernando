"""
CFG.py
Descripción. Genera, manualmente, el árbol de derivación
de la oración "Naomi come un taco"  
"""

from discopy.grammar.cfg import Ty, Tree, Rule, Word

n, v, a = Ty('N'), Ty('V'), Ty('A')
c, p, s = Ty('C'), Ty('P'), Ty('S')
Naomi, come = Word('Naomi', n), Word('come', v)
un, taco = Word('un', a), Word('taco', n)
C, P = Rule(a @ n, c), Rule(v @ c, p)
S = Rule(n @ p, s)
sentence = S(Naomi, P(come, C(un, taco)))
sentence.to_diagram().foliation().draw()