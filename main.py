num = 12
nmpt = 23.67
name = "Kunal"
bol = True
nmpt = str(23.67)
lst = [1,2,3,4,5,6,7,8,9,1,1,1,1,3,3,5,5,2,2,6]
tup = (0,9,8,7,6,5,4,3,2,1)

# print all variables (num to bol)
print(num,nmpt,name,bol)
# print all variables datatypes
print("Data types of all variables : ",type(num),type(nmpt),type(name),type(bol),type(lst),type(tup))

ind = lst.index(6)
print("Index number of Value : ",ind)

print("Value at this Index : ",lst[ind])
print("Length of List : ",len(lst),"Length of Tuple : ", len(tup))
lst.insert(5,90)
print("Inserted number 90 at 5th index","\n",lst)
lst.sort()
print("Sorted the List : ",lst)
lst.sort(reverse=True)
print("List in reverse : ",lst)
lst.remove(90)
print("Removed 90 from List : ",lst)
lst.pop(0)
print("Removed number at 8th index : ",lst)
lst.append(901)
print("Appended 901 : ",lst)
lst.insert(1,109)
print("Inserted 109 : ",lst)
print("Unique values with Set : ",set(lst))




