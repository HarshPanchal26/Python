import time
# What is Decorator 

    # A decorator is a design pattern in Python that allows you to wrap a function or class with another function, also known as a decorator function, to enhance or modify its behavior.
    
# How to define a decorator
    # One way 
from typing import Any


def decoreator_example(func):
    def addOne(): 
       value = func()
       return value + 1
    return addOne


# @decoreator_example
def dispaly():
    return 30

output_decp = decoreator_example(dispaly)

print(output_decp())



#  Another Way to define decorator 

    # Decorators are defined as higher-order functions, which are functions that take one or more functions as arguments and return a new function. The decorator function is typically defined with the @decorator_name syntax directly above the function it decorates.
    
def greeting_decorator(func):
    def wrapper():
        print("Hello!")
        func()
        print("Goodbye!")
    return wrapper

@greeting_decorator
def greet():
    print("Welcome to the party!")

greet()

# class base decorators 

    # Decorators can also be implemented as classes. To create a class-based decorator, the class needs to define the __call__() method, which allows instances of the class to be called as functions.

    # Here's an example of a class-based decorator that measures the execution time of a 
    
class Time_pass : 
    def __init__(self , func) -> None:
        self.func = func
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        start_time = time.time()
        result = self.func()
        end_time = time.time()
        total_time=end_time-start_time
        print("Executaion compelted in {:.1f}".format(total_time))
    
@Time_pass
def call_Time_pass():
    time.sleep(1)
    print("Computation completed")
    
call_Time_pass()


# Multiples decorators 


def subtract_from(func):
    def sub():
        value = func()
        return value - 2
    return sub

def add_from(func):
    def add():
        value = func()
        return value +1
    return add

@subtract_from
@add_from
def perform():
    return 0

print(perform())


#  How to pass a variable with decorators 


#  Basic three methods 

        # Approach 1: Decorator Factory
        # Approach 2: Nested Decorators
        # Approach 3: functools.wraps
        
    
            
def outer_func(sender_name):
    def deco_with_variable(func):
        def inner_body( *args, **kwargs):
            print("parameter data are args :{0} kwrgs : {1}".format(kwargs , args))
            value  = func(*args, **kwargs)+" "+sender_name 
            print(value)
        return inner_body
    return deco_with_variable

@outer_func("Decorators")
def display2(name):
    return f"I am {name} from"

display2("Harsh")




# While nested decorators and decorator factories achieve similar outcomes by allowing parameters to be passed to decorators, there are differences in their implementation and usage. Nested decorators involve defining multiple decorators and applying them in a chain, while decorator factories use a higher-order function to generate the decorator based on the provided arguments. Nested decorators have a specific order of execution, while decorator factories follow the order in which decorators are applied using the @ syntax.

# The choice between nested decorators and decorator factories depends on the specific requirements and design preferences of your code. Both approaches offer flexibility and the ability to customize the behavior of decorators, allowing you to create more versatile and reusable decorators.



        # Nested Decorators:
        
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Log: Function", func.__name__, "is called")
        return func(*args, **kwargs)
    return wrapper

def timer_decorator(func):
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Timer: Function", func.__name__, "took", execution_time, "seconds")
        return result
    return wrapper

@log_decorator
@timer_decorator
def greet(name):
    print("Hello,", name)

greet("John")



        #  Factory 
    
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Log: Function", func.__name__, "is called")
        return func(*args, **kwargs)
    return wrapper

def timer_decorator(func):
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Timer: Function", func.__name__, "took", execution_time, "seconds")
        return result
    return wrapper

@log_decorator
@timer_decorator
def greet(name):
    print("Hello,", name)

greet("John")



#  functool 


# Certainly! The functools.wraps decorator from the functools module is commonly used when creating decorators to preserve the original function's metadata such as its name, docstring, and signature. Here's an example:


import functools

def decorator_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function docstring."""
        print("Decorator executed!")
        return func(*args, **kwargs)

    return wrapper

@decorator_func
def greet(name):
    """Greet someone by name."""
    print("Hello,", name)

print(greet.__name__)
print(greet.__doc__)
