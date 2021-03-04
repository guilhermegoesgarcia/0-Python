


# a = 10
# b = 25
# c = 66
#
# x = int(input("Digite um numero: "))
#
# #if(x==a or x==b or x==c):
#
# if( x in [a,b,c]):
#     print("O numero está contido")
# else:
#     print("Não está contido")

# -----------------------------------------


cores = ["azul","amarelo","vermelho","branco"]

while True:
    cor = input(" Digite o nome de uma cor ou então,"
                  " n° 0 para sair do programa ")

    if (cor=="0"):
        break
    if cor in cores:
        print("Essa cor está contida!")
        print()

    else:
        print("Essa cor NÂO está contida!")
        print()