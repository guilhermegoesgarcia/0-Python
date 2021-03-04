
# Exceção .. erros de execução

try:
    a = 10/0

    print()
    print (a)
except ZeroDivisionError:
    print()
    print("Não é possivel Dividir um número por zero.")