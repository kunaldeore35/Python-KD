def sum(num):
    i = 0
    ans = 0
    while i < num:
        i = i+1
        ans = i + ans
    # print("The sum is ",ans)
    final = "The Sum is {}".format(ans)
    return final

print(sum(10))