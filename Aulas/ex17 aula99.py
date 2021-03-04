
lista = list(input("Escreva alguns numeros: "))

def func(n):
    num = lista
    a = 0 # contador de repetição do elemento
    p = 0 # contador de posição
    prox = 0 # comparador com o proximo elemento
    e = 0 # contador do ciclo
    total = len(n) # Numero total de elementos

    for c in lista:
        e += 1
        if (e <= len(n)):
         while (prox < total):

            if (c == lista[p]):
                a += 1
                p += 1
                if (a >= 2):
                 p -= 1
                 num.pop(p)

                 total -= 1

            else:
                 prox += 1


        p += 1
        prox = 0

    else:
            print("A nova lista de numeros não duplicados :")
            print(num)


func(lista)