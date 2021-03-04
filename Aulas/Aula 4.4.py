# Método - append   -- > add elemento na lista vazia

lista = []

#add elementos na lista
while True:
    n = int(input("Dígite um número ou '0' para sair: "))
    if n == 0:
        break

    lista.append(n)

k = 0

while k < len(lista):

    print(lista[k])
    k += 1

# removendo elementos

a = input("\nDeseja remover algum elemento da lista? s/n: ")

if a == "s" :
    x = int(input(" Digite o elemento: "))
    print(f"Elemento [{lista.pop(x-1)}] excluido!")
    print(f"Nova lista: {lista}")
elif a == "n":
    print("Programa Fim !!")