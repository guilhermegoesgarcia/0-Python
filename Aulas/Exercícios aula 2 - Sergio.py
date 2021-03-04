#Exercícios da Aula 2:
print("Exercício 1\n")
detergente=int(input("Quantas unidades de detergente estão disponíveis?: \n"))
sabao=int(input("Quantas unidades de sabão estão disponíveis?: \n"))
esponja=int(input("Quantas unidades de esponja estão disponíveis?: \n"))
kitdetergente=detergente//4
kitsabao=sabao//3
kitesponja=esponja//5
if kitdetergente<kitsabao and kitdetergente<kitesponja:
    kits=kitdetergente
elif kitsabao<kitdetergente and kitsabao<kitesponja:
    kits=kitsabao
elif kitesponja<kitdetergente and kitesponja<kitsabao:
    kits=kitesponja
else:
    kits=0
print(f"Poderão ser vendidos {kits} kits")

print("Exercício 2\n")
#<=3 anos - 2.5%*slr
#>3 anos - 2,5%*slr + 1,7% por ano
slr=float(input("Qual seu salário?: R$"))
ts=int(input("Quantos anos de serviço?: \n"))
if ts<=3:
    adicional=(slr*2.5/100)
else:
    adicional=(slr*2.5/100)+(slr*((ts-3)*1.7/100))
print(f"Seu adicional será de R${adicional:1.2f}")

print("Exercício 3\n")


print("Exercício 4\n")
distância=float(input("Qual a distância, em metros, do sofá até a televisão?: "))
série=int(input("A TV é Série 100 ou 200?: "))
if série==100:
    if distância<=2.8:
        tamanho=42
    elif 2.8<distância<=3.6:
        tamanho=50
    elif distância>3.6:
        tamanho=61
elif série==200:
    if distância<=1.4:
        tamanho=32
    elif 1.5<distância<=2.6:
        tamanho=37
    elif distância>2.6:
        tamanho=42
else:
    print("A série digitada não existe, tente novamente")
print(f"O tamanho ideal da sua TV é {tamanho} polegadas\n")

print("Exercício 5\n")
número=int(input("Digite um número com 3 algarismos: "))
x1=número//100%10
x2=número//10%10
x3=número//1%10

aritmética=(x1+x2+x3)/3
harmônica=3/((1/x1)+(1/x2)+(1/x3))
geométrica=(x1*x2*x3)**(1/3)

if aritmética>harmônica and aritmética>geométrica:
    maior=aritmética
    nome="aritmética"
elif harmônica>aritmética and harmônica>geométrica:
    maior=harmônica
    nome="harmônica"
elif geométrica>aritmética and geométrica>harmônica:
    maior=geométrica
    nome="geométrica"

print(f"A média aritmética é {aritmética:1.2f}")
print(f"A média harmônica é {aritmética:1.2f}")
print(f"A média geométrica é {aritmética:1.2f}")
print(f"A maior das médias é a {nome} e seu valor é de {maior:1.2f}")
