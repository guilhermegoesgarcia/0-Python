#Repetição While
print("\nBem vindo ao contador de numeros!\n")
n= int(input("Digite o ultimo numero: "))
x=1
total_impar =0
total_par = 0

while x <= n:
    if x%2 == 0:
        print(f"{x} é par")
        total_par += 1
    else:
        print(f"{x} é impar")
        total_impar += 1
    x += 1

print (f"\nTotal de elementos:\n Impar-> {total_impar} \n Par-> {total_par}")