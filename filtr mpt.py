lst = [3,3,4,3,4,4,8,5,"k","d","k",34.5,34.5,True,True,False]
# ** Remove Empty Values from List **
# for i in lst:
#     if [] in lst:
#         lst.remove([])
# print(lst)

for i in set(lst):
    con = lst.count(i)
    # lst = list(lst1)
    print("Element : ",i,"is ",con,"Times")
# inp = input("Enter the Value Pencho : ")
# print(inp)