
# bloqueando os membros .. (uso restrito da imagem)

class Retangulo:

    def __init__(self,largura,altura):
        self._largura = 0 # não deve ser acessado diretamente.. só pelo metodo SET ou GET
        self._altura = 0
        self.__var = 0 # o nome desse membro deve ser desfigurado .. porem só externamente
        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self, num): # verifica se o valor e do tipo inteiro
        if(not(isinstance(num,int) and(num > 0))):
            raise ValueError("Altura é Inválida: {}".format(num))
        self._altura = num
        self.__var = 456 # não sofreu alteração

    def set_largura(self,num):
        if(not(isinstance(num,int) and(num > 0 ))):
            raise ValueError("Largura é Inválida: {}".format(num))
        self._largura = num

    def get_area(self):
        return self._altura * self._largura

r = Retangulo(largura = 10, altura = 5)
#r = Retangulo(largura = 10, altura = -5)

print()
print("Área = {}".format(r.get_area()))

r.