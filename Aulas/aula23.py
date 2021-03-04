
print()
print()
a = int(input("digite um numero para ser elevado ao Quadrado e ao Cubo: "))

def potencia(x):
    quadrado = x**2
    cubo = x**3

    return quadrado,cubo

q,c = potencia(a)

print()
print("Quadrado:",q)
print("Cubo",c)
print()
