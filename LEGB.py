#  Local , Enclosing , Global , Built-In

x = "I am Global Function"
def OuterFunxtion():
    x = "I am Outer Value" 
    
    def InnnerFunction():
        nonlocal x
        x = "I am Inner Fuction changed by InnerFunction"

        print(x)
    print(x)
    InnnerFunction()
    print(x)
    
OuterFunxtion()


# The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function. Use the keyword nonlocal to declare that the variable is not local.


# Globla and Local are used to bind variable with thier respective Enclosing environmant 