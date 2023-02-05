def incdesc(lst):
    ln = len(lst)
    asc = False
    desc = False

    for i in range(ln-1):
        if lst[i] < lst[i+1]:
            asc = True
        else:
            asc = False
            break
    for i in range(ln-1):
        if lst[i] > lst[i+1]:
            desc = True
        else:
            desc = False
            # break
    if asc or desc == True:
        print("Monotony")
    else:
        print("Not monotony")

lst = [1,2,3,4,5,6,7,8]
incdesc(lst)
