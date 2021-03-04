
# copia de simbulos de ouotro modulo

# apartir deste modulo importe os simbulos
# FROM [modulo] IMPORT [simb]

# importar o modulo e utilizar outra forma de chama-lo (renomea-lo)
#IMPORT [modulo] AS [M]

# Renomeando simbolo
# FROM [modulo] IMPORT [simbolo] AS [S], [simb2] AS [S2]

#importa todos os simbolos de math
from math import *


from math import pi,e
# ou
# e = math.e

def func():
    from math import factorial
    print(factorial(5))


func()



from math import sqrt #square

print()
print(sqrt(9))
print()
print(pi)
print(e)

