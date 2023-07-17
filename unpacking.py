# Unpacking a List or Tuple:
    
values = [1, 2, 3]
a, b, c = values

# Unpacking a List or Tuple with Extended Unpacking:

values = [1, 2, 3, 4, 5]
a, *b, c = values
print(b) #  0utput 2 3 4 

# Unpacking in Function Calls:

def add(a, b, c):
    return a + b + c

values = [1, 2, 3]
result = add(*values)


# Unpacking in Dictionary Creation:

keys = ['name', 'age', 'city']
values = ['John', 25, 'New York']
person = {k: v for k, v in zip(keys, values)}

# Unpacking in Function Calls with Keyword Arguments:
newdic = {"name" : "hasrh" , "age" : 12, "city" : "surat"}

def greet(name, age, city):
    print(f"Hello, {name}! You are {age} years old and from {city}.")

person = {'name': 'John', 'age': 25, 'city': 'New York'}
greet(**newdic)


