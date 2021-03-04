
# aula 127_ encapsulamento


class Retangulo:

    def __init__(self, largura, altura):
        self.a = largura
        self.l = altura

    def area(self):
        return self.a * self.l

r = Retangulo(10, 5)
# r.l = "teste"     ERRO


print(r.area())
