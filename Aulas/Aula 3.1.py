# Acumuladores

n = 1
soma = 0
k = int(input("\nDigite quantos numeros você deseja somar:"))

while n<=k:
    x= int(input(f"Digite o {n} número: "))
    soma=soma+x
    n=n+1
    print(f"Soma:{soma}")

print(f"\nMédia: {soma/k:5.2f}")