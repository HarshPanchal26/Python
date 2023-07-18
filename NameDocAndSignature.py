#  Name , Signature and DocString the metadata of any fuction or methos in python 


# ṇame 

# The name of a function or method is its identifier, which is used to refer to and call the function. The name provides a unique way to identify the function within the code. In Python, you can access the name of a function using the __name__ attribute.

# For example:

def greet(name):
    print("Hello,", name)

print(greet.__name__)  # Output: greet



#  DocString 

# The docstring, short for "documentation string," is a string literal specified as the first statement within a function or method definition. It serves as a way to document the purpose, usage, and behavior of the function. Docstrings provide a convenient way for developers to understand how to use the function and can be accessed using the __doc__ attribute.


def greet(name):
    """Greet someone by name."""
    print("Hello,", name)

print(greet.__doc__)  # Output: Greet someone by name.


# signature

# he signature of a function or method describes its parameter structure, including the number, names, and types of parameters it accepts, as well as its return type. The signature provides information about the function's interface and helps ensure proper usage. In Python, you can access the signature of a function using the inspect module or other third-party libraries like signature from the inspect module or getfullargspec from the inspect module.


import inspect

def greet(name):
    """Greet someone by name."""
    print("Hello,", name)

signature = inspect.signature(greet)

print(inspect.isgenerator(greet))
print(signature)  # Output: (name)


