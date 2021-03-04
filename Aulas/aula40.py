# Como capturar a instância do erro

def erro(x) :
    try:
        eval(x)
    except (TypeError,NameError):     # TRATAMENTO PARA MAIS DE UM ERRO
        print("TypeError ou então , NameError..")

    except ValueError as e:

        print("ValeuError..")
        print(type(e)) # instancia da exceção
        print(e.args) # argumentos das mesagens
        print(e) #__str__ mensagem

    except ZeroDivisionError:

        print("ZeroDivisionError..")

'''' #TypeError
erro("int+int")

 #NameError
erro("a")
'''

 #ValueError
erro("int('a')")


''''
 #ZeroDivisionError
erro("5/0")
erro("10+10")
'''

print()
print("A execução foi finalizada!!")