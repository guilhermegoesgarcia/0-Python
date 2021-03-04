#Lsta - cálculo das médias

notas = [5,2,8,7,9,0]

soma = 0
k = 0

while k < len(notas):
    soma += notas[k]
    k += 1

print(f"\nSoma: {soma}")
print(f"Média: {soma/len(notas):5.2f}")
