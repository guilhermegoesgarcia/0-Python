
# Declaração de membros_ OBJ


class Retangulo:



    def area(self):
        return self.a * self.l


def membros_retangulo (r):
        r.a = 0
        r.l = 0


r1 = Retangulo()
membros_retangulo(r1)
r1.l = 10
r1.a = 5

#r2 = Retangulo()
#r3 = Retangulo()



print(r1.area())