
def func():
    var_local = 10
    def func_interna():
        nonlocal var_local
        var_local +=1
        print(var_local)

    func_interna()

func()

x=10
def funcX():
    global x
    return x
print(funcX())