
# Getters E Setters

class Retangulo:

    def __init__(self,largura,altura):
        self.largura = 0
        self.altura = 0
        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self, num): # verifica se o valor e do tipo inteiro
        if(not(isinstance(num,int) and(num > 0))):
            raise ValueError("Altura é Inválida: {}".format(num))
        self.altura = num

    def set_largura(self,num):
        if(not(isinstance(num,int) and(num > 0 ))):
            raise ValueError("Largura é Inválida: {}".format(num))
        self.largura = num

    def get_area(self):
        return self.altura * self.largura

r = Retangulo(largura = 10, altura = 5)
#r = Retangulo(largura = 10, altura = -5)

print()
print("Área = {}".format(r.get_area()))

