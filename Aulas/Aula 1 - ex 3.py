print("\n Bem vindo ao Conversor de temperatura °C para °F")
n = int(input("Digite:  1 para ºC ou 2 para °F: "))
x = int(input("Digite a Temperatura: "))
if n == 1:
    T = ((9*x)/5)+32
    print(f"Temperatura: {T}ºF ")
elif n == 2:
    T =((x-32)*5)/9
    print(f"Temperatura: {T}°C")
else:
    print("Digito Invalido !! ")


