def prime(num):
    lst = []
    for i in range(1,num+1):
        flag = False
        for j in range(2,i):
            if i%j ==0:
                flag = True
                break
        if flag == False:
            lst.append(i)
    print(lst)

prime(19)
