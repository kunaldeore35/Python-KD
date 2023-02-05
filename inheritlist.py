lstin = [[1,2,True,2.2],[False,True, 8.6, 2.2],["k","d",1,2],["k","d",7,8]]
l = []
lg = len(lstin)
# print(lg)
for i in range(lg):
    for j in lstin[i]:
        l.append(j)
s = set(l)
print(list(s))
