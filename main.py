
def my(name) : 
    print(name)
    # Bitwise operations 
    #    print(5 & 1) 
    user_permissions = 0b0100 + 0b0010      
    print(user_permissions)

    print(f"Bigad gaye the ishq mai thode bohot \
        Dill tota useke bad \
        Dill tode bohot {name}")   
        
if 3>4 : 
    print("Hash is sexy")
elif 3==3:
    print(f"Both 3's are same , Wow") 
else :
    my("Hello form Harsh")
    print('Hello from outside of line')
        
    

for i in range(0 ,11 ,5):
    if i%2 == 0 :
       print(i)
    else:
       print("Not a even number sorry ~!!!!!!!!!1")   


# in raange for loop exclude the last the lasr elenent and include the inculded 


for i in range(10,0, -1):
    if i == 1 :
        print("NUM... Blastoff")
    else :
        print(i)


# list 

lists =  ["Harsh", "Manan" , "Jenish" , "Doreamon(Jenish no mal)"]

print(len(lists))

# length of list here

#  Update list
lists[3] = "shivangi(Jenu no maal)"

lists.append('Yogita(Manan ka maal)')
lists.pop(len(lists)-2)


for item in lists : 
    print(item)
    
old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
new_character_levels = [1, 42, 41, 52, 12, 3, 32, 12, 54, 32, 43]

# concatenate lists 

print(old_character_levels + new_character_levels)
# don't touch above this line

for i in range(0, len(old_character_levels)):
    if old_character_levels[i] != new_character_levels[i]:
        print(i)

print(old_character_levels[1:5])
# print(item)


#  list operation contains 

print("harsh" in lists)

#  list operation with del

del lists[len(lists)-1]

#   used for reverse string
print(lists[::-1]) 

#  we can also modify list with slice operation using del




#  #####################  Tuples 

# Tuples are collections of data that are ordered and unchangeable. You can think of a tuple as a List with a fixed size. Tuples are created with round brackets:

# While it's typically considered bad practice to store items of different types in a List it's not a problem with Tuples. Because they have a fixed size, it's easy to keep track of which indexes store which types of data.

# Tuples are often used to store very small groups (like 2 or 3 items) of data. For example, you might use a tuple to store a dog's name and age.


tuples = ("Harsh" , 21 , "Berojgar for now")

# Tuples inside list 


my_tuples = [("this is the first tuple in the list", 45, True),("this is the second tuple in the list", 21, False)]
print(my_tuples[0][0])

# If we did not return anything in function then it should default have a value flase(returned value) ,

# And if we return multiple value then it might return tuples 

def newFunction(name = "Harsh") : 
    print(f"I am doing nothing ans returning nothing ,created by the {name}")
    return "Hi", "My name is" , "Harsh"
result = newFunction()

print(type(result))



def doubleLatters(string) :
    for char in string:
        
        print(int(char) + 2)

# doubleLatters("Harsh")


############################ Dictionary ######################


# Dictionaries in Python are used to store data values in key -> value pairs. Dictionaries are a great way to store groups of information.


car = {
  "brand": "Tesla",
  "model": "3",
  "year": 2019
}

car["name"] = "Range Rover"

print(car["name"].split('R'))

#  for delete recoerds from dicionary 

del car["year"]

print(f"car {car}")


#  to check whether dictonary has a key in it ot not 


if "year" in car : 
    print("Year is here ")
else :
    print('No Year is has not been mentioned in this list')
    


names = ["jack bronson", "jill mcarty", "john denver"]

names_dict = {}
for name in names:
    # .split() returns a list of strings
    # where each string is a single word from the original
    names_arr = name.split()

    # here we update the dictionary
    names_dict[names_arr[0]] = names_arr[1]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty', 'john': 'denver'}



# sets    , brother of list and tupples , ceated with {}




# Sets are like Lists, but they are unordered and they guarantee uniqueness. There can be no two of the same value in a set.

sets = {"hi", "hell0o", "bye "}

list2 = ["hi", "hell0o", "bye ", "bye"]

print(list(set(list2)))


newList =[
        "fireball",
        "eldrich blast",
        "fireball",
        "eldrich blast",
        "water gun"]

unique_data = set(newList)

print(list(unique_data))



# Because the {} syntax creates an empty dictionary, to create an empty set, just use the set() function.

# fruits = {}  this will show an error because it will might act as an empty dictonary !!! Cool 
fruits = set()

fruits.add("apple")
fruits.add("apple4")
fruits.add("apple2")
fruits.add("apple3")

fruits.remove('apple')
# ITERATE OVER VALUES IN A SET (ORDER IS NOT GUARANTEED)
print(fruits)

mango = {}

mango["name"] = "Kesar"
print(mango)


string = "Harsh Panchla is here"

for ch in string.split():
    print(ch)