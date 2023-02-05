def hapy(num):
    dup = set()

    while True:
        if num !="1" and str(num) not in dup:
            sum = 0
            dup.add(str(num))
            for i in str(num):
                sum = sum + int(i) ** 2
                # print(sum)
            num = str(sum)
        elif num in dup:
            print("UnHappy Number")
            break
        else:
            print("Happy Number")
            break

hapy(14)