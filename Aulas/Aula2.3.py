#Categoria de preços

print("\nCategorias 1 ate 5")
categoria = int(input("\nDigite a categoria: "))

if categoria == 1:
    preço = 10
    print (f" Preço do produto R${preço: 5.2f}")
elif categoria == 2:
    preço = 18
    print(f" Preço do produto R${preço: 5.2f}")
elif categoria == 3:
    preço = 23
    print(f" Preço do produto R${preço: 5.2f}")
elif categoria == 4:
    preço = 26
    print(f" Preço do produto R${preço: 5.2f}")
elif categoria ==5:
    preço = 31
    print(f" Preço do produto R${preço: 5.2f}")
else:
    print("Categoria Inválida !!")
