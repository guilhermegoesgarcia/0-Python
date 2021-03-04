print("\nCálculo da conta de telefone ! ")

minutos = float(input("\nDigite o valor da sua conta:"))
if minutos < 200:
    conta = minutos * 0.2
    print(f"Valor da conta: R${conta: 5.2f}")
elif 200<= minutos and minutos <= 400:
    conta = minutos * 0.18
    print(f"Valor da conta: R${conta: 5.2f}")
elif minutos > 400:
    conta = minutos * 0.15
    print(f"Valor da conta: R${conta: 5.2f}")

