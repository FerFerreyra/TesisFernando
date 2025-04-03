"""
reg.py
Descripción. Se implementa una gramática simple, mediante su
signatura y una función de validación de oraciones dentro de la gramática.
Se efectúan ejemplos de cómo funciona. 
"""

from discopy.utils import AxiomError
from discopy.cat import Ob, Arrow, Box

#Definimos la signatura que genere la gramática
s0, x0, x1, x2, x3, s1 = map(Ob, "s0 x0 x1 x2 x3 s1".split())
A,B = Box('A', s0, x0), Box('B', s0, x0)
conoce = Box('conoce', x0, x1)
a = Box('a', x1, x2)
C,D = Box('C', x2, x3), Box('D', x2, x3)
quien = Box('quien', x3, x0)
_ = Box('.', x3, s1)
gramatica = [A, B, conoce, a, C, D, quien, _]

#Definimos valida_gramatical que dada una oración y una gramatica
#determina si la oración es válida en la gramática 
def valida_gramatical(oracion, gramatica):
    flecha = Arrow.id(s0)  # Inicializamo la identidad en s_0
    bandera = True 
    oracion = oracion.split() + ['.']  # Agregamos un punto al final de la oración
    for palabra in oracion:
        # Intentamos encontrar una Box en la gramática que coincida con la palabra actual
        es_Box = False
        for Box in gramatica:
            if Box.name == palabra:
                try:
                    flecha = flecha.then(Box)  # Componemos la flecha con la Box
                    es_Box = True
                    break  # Si la composición es correcta, continuamos
                except AxiomError:
                    bandera = False  
                    break  # Terminamos la búsqueda si no es posible componer
        if not es_Box:
            bandera = False  # Si no encontramos ninguna Box que coincida, no es oración
            break
    return bandera

oraciones = ["A conoce a D", "A conoce a D quien conoce a C", "A conoce a B"]

for oracion in oraciones:
    valida = valida_gramatical(oracion, gramatica)
    print(valida)