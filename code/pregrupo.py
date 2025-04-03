"""
pregrupo.py
Descripción. Realiza una sencilla derivación en una gramática de pregrupo.
"""

from discopy.grammar.pregroup import Ty, Word, Cup

s, n = Ty('s'), Ty('n')
Octavio, amor = Word('Octavio', n), Word('amor', n)
envió = Word('envió', n.r @ s @ n.l)

sentence = Octavio @ envió @ amor >> Cup(n, n.r) @ s @ Cup(n.l, n)
sentence.draw()