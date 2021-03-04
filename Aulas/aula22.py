
#introdução a função

def soma(x,y):

    total = x+y

    print()
    print()
    print("O total da soma é : !!", total)
    print()
    print()

#soma(10,50)


def login (usuario="root",senha="123"):
    print("usuario:", usuario)
    print("senha:", senha)

#login()

def dados_pessoais (nome,sobrenome,idade,sexo):
    print(" Nome: {}\n Sobrenome: {}\n Idade: {}\n Sexo: {}"
            .format(nome,sobrenome,idade,sexo))

#dados_pessoais("Cláudio","Rogério",30, True)

dados_pessoais(nome="Claudio",
               sobrenome="Carvalho",
               idade=30,
               sexo=True)