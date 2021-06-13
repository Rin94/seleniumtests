"""
What is python closure?
When we define a function inside of another, the inner function is said to be
nested inside the outer one.
"""
def outerfunc(x):
    def innerfunc():
        print(x)
    return innerfunc

def outerDecorator(funcionParametro):
    def funcionInterior(*args):
        print("resultado de la operacion")
        result=funcionParametro(*args)
        print("Resultado: ",result)
        print("Fin de la funcion decoradora")
    return funcionInterior

@outerDecorator
def inner(x,n):
    result=0
    while n > 0:
        result += x * n
        n -= 1
    return result


def outer(x):
    result=0
    def inner(n):
        nonlocal result
        while n>0:
            result+=x*n
            n-=1
        return result
    return inner

if __name__ == '__main__':

    inner(7,3)
    #myFunc=outer(7)
    #print(myFunc(3))
    #myFunc()
    """
    A python closure is when some data gets attached to the code
    the value is remembered even when the variable goes out of scope, or
    the function is removed from the namespace
    """
    #del outerfunc
    #myFunc()