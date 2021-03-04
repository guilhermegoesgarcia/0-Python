# Copiando Listas

lista1 = [1,3,"A"]
lista2 = lista1[:]  # copia apenas o conteudo.. mantendo indereços diferentes

print(f"\nLista 1: {lista1}")
print(f" Lista 2: {lista2}")

lista1[0] = 8
print(f"\nLista 1: {lista1}")
print(f" Lista 2: {lista2}")