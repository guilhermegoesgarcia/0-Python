# Incerindo informação na lista

notas = [0,0,0,0,0,0]

soma = 0
k = 0

while k < len(notas):
    notas[k] = float(input(f"Nota elemento [{k}]: "))     #Lendo notas
    soma += notas[k]
    k += 1

print(f"\nSoma: {soma}")
print(f"Média: {soma/len(notas):10.2f}")