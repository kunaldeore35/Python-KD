eve = []
odd = []
for a in range(1, 101):
    if a % 2 == 0:
        eve.append(a)
    else:
        odd.append(a)

print("Even List : ",eve)
print("Odd List : ",odd)
