l = int(input('beginning of the interval: '))
u = int(input('end of the interval: '))



for num in range(l, u+1):
    if num > 1:


        for i in range(2, num):
            if num%1 == 0:
                break
        else:
            print(num)



