
print("\n Ordenação de numeros.\n")
numero1 = float(input("Entre com um número: "))
numero2 = float(input("Digite outro número: "))

if numero1 > numero2:
    print(f"\nO {numero1} é maior que {numero2}")
if numero2 > numero1:
    print(f"\nO numero {numero2} é maior que o {numero1}")

if numero1 == numero2:
    print("\nOs dois numeros são iguais !")