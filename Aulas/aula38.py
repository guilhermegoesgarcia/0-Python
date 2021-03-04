# tratamento de múltiplas exceções.. Aula 113

def erro(x) :
    try:
        eval(x)
    except TypeError:
        print()
        print("TypeError..")
    except NameError:

        print("NameErro..")
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