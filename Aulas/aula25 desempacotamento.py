
def pessoa (nome, sobrenome,idade):
    print()
    print("Nome:",nome)
    print("Sobrenome:",sobrenome)
    print("Idade:",idade)

#lista = ["eXcript","Brasil",20]

#pessoa(tupla[0],tupla[1],tupla[2])
#pessoa(*lista)


d = {"sobrenome":"Brasil","idade":30,"nome":"eXcript"}
pessoa(**d)