#  Here we are going to leran traversing list 
nums = [10,9,8,7,6,5,4,3,2,1]

lists = []

for n in nums :
    lists.append(n)



#   comprehension with lists

lists_com = [n for n in nums]

print(lists_com)

#  line if code for getting even numbers 

lists_even = [ n for n in nums if n%2 == 0]
print(lists_even)

# return the tuples inside list (letter , range) where range is between 0 to 4

list_nested = [(letter , nums) for letter in 'harsh' for nums in range(2)]
print(list_nested)



