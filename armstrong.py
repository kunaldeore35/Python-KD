# b = 0
# i = 0
# ln = len(str(i))
# for i in range(200):
#     b += int(i) ** ln
#     print(b)


def armstrong(num):
    result = 0
    snum = str(num)
    ln = len(snum)
    for i in snum:
        result += int(i) ** ln
    if result == num:
        return True
    else:
        return False

lst = []
for j in range(1,10000):
    if armstrong(j) == True:
        lst.append(j)
print("Armstrong Number List",lst)
