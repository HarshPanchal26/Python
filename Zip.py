bfs = ["Manan" , "Harsh" , "Jenish" , "Ronak" , "Vatsal"]
gfs = ["Yogiya" , "Shraddha" , "Doramon" , "Priya" , "Bhatiya"]

bf_gf = [zip(bfs , gfs)]
print(bf_gf)
print(sorted(zip(bfs , gfs)))

#  sorted will retur a list 

# Zip by default return an object , so we can not print it simpaly otherwise it give us 
# <zip object at 0x0000018D67F5ED40> somthing like this 

#  we have to convert it in to the list 

list_zip = [n for n in zip(bfs , gfs)]
print(list_zip)




# Dictonary 
dic = {}

for boys,girl  in zip(gfs,bfs):
        dic[boys] = girl

print(dic)


# Easy methos 

dic = {boys : girl for boys,girl  in zip(gfs,bfs)}
print(f"my dic is {dic}")


#  Sets
nusm = [1,1,3,3,4,5,5,7,8]
    
print([n for n in set(nusm) if n%2!=0])


print("Harah6" + str(9))      