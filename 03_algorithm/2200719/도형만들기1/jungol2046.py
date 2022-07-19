n, m = map(int, input().split())

if m == 1:
    for i in range(1,n+1):
        for j in range(n):
            print(i, end=' ')
        print()

elif m == 2:
    for i in range(n):
        if i % 2 == 0:
            for j in range(1,n+1):
                print(j, end = ' ')
            print()
        else:
            for j in range(n,0,-1):
                print(j, end = ' ')
            print()

elif m == 3:
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i * j, end = ' ')
        print()