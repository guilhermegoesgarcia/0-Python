
# helo this program calcula numeros fatoriais

print()
num = int(input("Digite um numero para calcular seu fatorial: "))
print()

def fatorial(n):
    a = n-1
    while (a>0):

        n = n*a
        a = a-1

    print("O Numero %d! é: %d"%(num,n))

fatorial(num)
