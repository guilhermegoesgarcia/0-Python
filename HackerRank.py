
s = [
    [4,8,2],
    [4,5,7],
    [6,1,6]]

def formingMagicSquare(s):

    c=s[1][1]
    b=-c+s[2][2]
    a=c-s[0][2]

    q =[
        [c-b,c+a+b,c-a],
        [c-a+b,c,c+a-b],
        [c+a,c-a-b,c+b]
    ]

    # metodo soma das linhas
    l0= abs(sum(q[0])-sum(s[0]))
    l1 = abs(sum(q[1]) - sum(s[1]))
    l2 = abs(sum(q[2]) - sum(s[2]))

    somaL =sum([l0,l1,l2])

    # metodo comparação por elemento

    somaE=0; cont0=0;  cont1=0;

    while cont0<=3:

        for x in range(3):
            somaE+= abs(s[x][cont1]-q[x][cont1])
            cont1+=1

        cont1=0
        cont0+= 1

    if somaL < somaE and somaL != 0:
        return somaL
    elif somaL > somaE and somaE != 0:
        return somaE
    elif somaE != 0:
        return somaE
    elif somaL != 0:
        return somaL
    else:
        return somaE




print(formingMagicSquare(s))


