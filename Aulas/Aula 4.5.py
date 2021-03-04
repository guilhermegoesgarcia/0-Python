# Fila - inclusão no fim e remoção no início.

ultimo = 10

fila = list(range(1,ultimo+1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila ")
    print(f"Fila atual:{fila}")
    print(f"Digite Fila-> F .. Atendido -> A .. Sair -> S ")
    operacao= input("Digite F,A ou S:")
    if operacao == "A" or operacao == "a":
        if len (fila)> 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia")

    elif operacao == "F" or operacao == "f":
        ultimo += 1
        fila.append(ultimo)
    elif operacao == "S" or operacao == "s":
        break

    else:
        print("Operação inválida! Digite F, A ou S..")
