def npr(n,k):
    if n == k:
        print(*p)
    else:
        for i in range(n,k):
            p[n], p[i] =p[i], p[n]
            npr(n+1,k)
            p[n], p[i] =p[i], p[n]


p = [i for i in range(1, 4)]
npr(0,3)