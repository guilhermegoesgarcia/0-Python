# tratamento de valores invalidos .. Ex: digitado pelo usuario


def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print()
            print(" Número inválido...")


print()
num1 = input_float("Digite o primeiro número: ")
num2 = input_float("Digite o segundo número: ")

try:
    print("  Resultado :", num1/num2)
except ZeroDivisionError:
    print()
    print(" Não é possível dividir um número por zero..")