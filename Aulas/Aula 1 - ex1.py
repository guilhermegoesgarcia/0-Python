
print('\n')
print("Calcule o aumento de sálario..")
print('\n')

a = int(input("Digite o seu sálario: "))
b = input("Digite a porcentagem de aumento: ")

#Contador
n = len(b)
indice = 0

#Fatiador
'''while indice <= n:
    if b[indice] == "%":
        b = b[0,indice]
    print(b)
    indice +='''


b = int(b)

a1 = a*b

print(f"\n Salario atual: {a1}")