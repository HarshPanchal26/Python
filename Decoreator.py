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