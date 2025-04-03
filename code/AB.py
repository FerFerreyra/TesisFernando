"""
AB.py
Descripción. Se realiza la derivación en una gramática AB de la oración
"Octavio envió una carta a su amada"
"""

from discopy.closed import Ty
from discopy.grammar.categorial import Word, BA, FA

s, n = map(Ty, 'sn')

Octavio = Word('Octavio', n)
envió = Word('envió', n >> (s << n))
una = Word('una', n << n)
carta = Word('carta', n)
a = Word('a', (s >> s) << n)
su = Word('su', n << n)
amada = Word('amada', n)

sentence = Octavio @ envió @ una @ carta @ a @ su @ amada\
    >> BA(n >> (s << n)) @ FA(n << n) @ ((s >> s) << n) @ FA(n << n)\
    >> FA(s << n) @ FA((s >> s) << n)\
    >> BA(s >> s)

sentence.draw()
