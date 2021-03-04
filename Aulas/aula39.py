
# Tratamento de Múltipas exceções... parte 2
# Tratamento iguais para erros diferentes



def erro(x) :
    try:
        eval(x)
    except (TypeError,NameError):     # TRATAMENTO PARA MAIS DE UM ERRO
        print("TypeError ou então , NameError..")

    except ValueError:

        print("ValeuError..")
    except ZeroDivisionError:

        print("ZeroDivisionError..")

 #TypeError
erro("int+int")

 #NameError
erro("a")

 #ValueError
erro("int('a')")

 #ZeroDivisionError
erro("5/0")
erro("10+10")

print("A execução foi finalizada!!")