n = int(input())
if n<1 or n>100 or n % 2 == 0:
    print("INPUT ERROR")
else:
    array = [[0]*i for i in range(n,0,-2)]

    num = 65


    for i in range(n//2,-1,-1):
        for j in range(0,n-i*2):
            array[i][j] = chr(num)
            num += 1
            if num > 90:
                num = 65

    for i in range(n//2+1):
        for j in range(i+1):
            print(array[j][i-j], end = ' ')
        print()
    for i in range(n//2+1,1,-1): # 3 , 2
        for j in range(i-1): # 2, 1
            print(array[j][j-i+1], end = ' ')
        print()