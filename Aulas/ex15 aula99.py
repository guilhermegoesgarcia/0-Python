
# Calcula a quantidade de letras Mausculas e minusculas

pala = list(input(" Escreva uma palavra :"))

def cont(n):
    lista_1 = list("qwertyuiopasdfghjklçzxcvbnm")
    lista_2 = list("QWERTYUIOPASDFGHJKLÇZXCVBNM")
    lista_3 = list("0123456789")

    f = len(pala)
    a = 0
    b = 0
    d = 0
    # faz o laço de repetição, colocando cada elemendo da lista "pala" na variavel "c".
    # FOR (var) IN (LISTA)
    for c in pala:
        if (c in lista_1):  # Verifica se a var "c" esta contido na lista
                a += 1
        if (c in lista_2):
                b += 1
        if (c in lista_3):
                d += 1

    print()
    print(" Essa palavra possui:")
    print("    %d letras Maiusculas" % (b))
    print("    %d letras minusculas" % (a))
    print("    %d Numeros" %(d))
    print()
    print("Total de %d Caracteres!"%(f))

cont(pala)
