
# Classe Retangulo _ aula 124


class Retangulo:

    def __init__(self):
        self.a = 0
        self.l = 0

    def area(self):
        return self.a * self.l


r1 = Retangulo()
r1.l = 10
r1.a = 5

#r2 = Retangulo()
#r3 = Retangulo()



print(r1.area())