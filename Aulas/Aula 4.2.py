#Lista Indefinida

numeros = [0,0,0,0,0]

k = 0

while k < len(numeros):
    numeros[k] = int(input(f"Número {k+1}:"))
    k += 1

while True:
    escolhido = int(input("\nQual posição você gostaria de imprimir?  ( digite '0' para sair ) "))
    if escolhido == 0:
        break
    print(f"Você escolheu o número: {numeros[escolhido - 1]}  ")



