#  String can be fromated in many ways in python 

# String Interpolation with f-strings:
name = 'John'
age = 25
city = 'New York'
sentence = f"Hello, my name is {name}, I am {age} years old, and I live in {city}."


#  normal way
name = " Harsh"
age = 12
sentence = "Hello my name is " + name + "and I am" + str(age) + "year old"
print("Hello my name is " + name + "and I am" + str(age) + "year old")



#  abnormal ways 

sentence = "Hello my name is {} and I am {} year old".format("Manana" , 51)
print(sentence)

#  By index number
sentence = "Hello my name is {1} and I am {0} year old".format("Manana" , 51)
print(sentence)

#  Default value
sentence = "Hello my name is {name} and I am {age} year old".format(name="Abhi" , age=41)
print(sentence)

#  If Dictonary is there 

dic = {name: "Jensih" , age : 22}

print("Hello my name is {0} and I am {1} year old".format(dic[name] , dic[age]))


dic = {"name": "Jensih no maal", "age": 22}
sentence2 = "Hello, my name is {0[name]} and I am {0[age]} years old".format(dic)
print(sentence2)



# The double asterisks (**) in the code you provided are used to unpack a dictionary in Python. This syntax is called dictionary unpacking or keyword argument unpacking.

dic = {"name": "Gogi", "age": 42}
sentence2 = "Hello, my name is {name} and I am {age} years old".format(**dic)
print(sentence2)




#  with for loop 



#                                   Colon (:)


# The colon (:) in string formatting is used to specify formatting options for the value being inserted into the string. It allows you to control how the value is displayed within the formatted string.

# When using the format method or f-strings, you can include a colon followed by formatting instructions inside the curly brackets {} that enclose the variable or expression to be formatted.

name = "J"
sentence = "Hello, {:10}!".format(name)
print(f"dddfff{sentence}")
# Output: "Hello, John !"

# In this example, the :10 specifies a minimum field width of 10 characters for the formatted value. The value, in this case, is the variable name which is left-aligned within the 10-character field.


#           Specifying Precision for Floating-Point Numbers:

# Formatting with Padding and Alignment: 

number = 103343
sentence = "The answer is {:>5}".format(number)
print(sentence)

# Output: "The answer is 42"

# In this example, :>5 right-aligns the value (number) within a field of width 5 characters. Any extra space is padded with empty spaces.

for n in range(1 , 10):
    # print("Hello I am {}".format(n))
    # print("Hello I am {0}".format(n))
    # print("Hello I am {:.3f}".format(n))   
    print("Hello I am {:,}".format(10**5))   
    print("Hello I am {:,.2f}".format(10**5))   
    
# Learn about datatime 

