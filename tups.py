tup = (1,2,3,4,"kd","kunal")
tu = len(tup)
t = list(tup)
print(tu)
if tu%2==0:
    t.insert(0,"messi")
    k = tuple(t)
else:
    t.pop(0)
    k = tuple(t)
print(k)


