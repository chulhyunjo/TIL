n, m = map(int, input().split())
if 0<=n<=100:
    if m == 1:
        for i in range(1,n+1):
            for j in range(i):
                print('*', end = '')
            print()

    elif m == 2:
        for i in range(n, 0, -1):
            for j in range(i):
                print('*', end = '')
            print()

    elif m == 3:
        for i in range(1, n+1): # 1, 2, 3, 4, 5
            for j in range(n-i,0,-1):
                print(' ' , end = '')
            for j in range(2*i-1):
                print('*', end = '')
            print()
    else:
        print("INPUT ERROR!")
else:
    print("INPUT ERROR!")