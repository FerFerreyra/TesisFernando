"""
combinatoria.py
Descripción. Se realiza la derivación en una gramática AB de la oración
"Octavio envió a su amada una carta"
"""

from discopy.closed import Ty
from discopy.grammar.categorial import Word, BA, FA, FX, BX

s, n = map(Ty, 'sn')

Octavio = Word('Octavio', n)
envió = Word('envió', n >> (s << n))
una = Word('una', n << n)
carta = Word('carta', n)
a = Word('a', (s >> s) << n)
su = Word('su', n << n)
amada = Word('amada', n)

sentence = Octavio @ envió @ a @ su @ amada @ una @ carta\
            >> BA(n >> (s << n)) @ ((s >> s) << n) @ FA(n << n) @ FA(n << n)\
            >> (s << n) @ FA((s >> s) << n) @ n\
            >> BX(s << n, s >> s) @ n\
            >> FA(s << n)

sentence.draw()