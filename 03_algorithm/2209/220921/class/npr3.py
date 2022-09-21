def f(i,k,r):
    if i == r:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                f(i+1,k,r)
                used[j] = 0
N = 5
R = 3
a = [i for i in range(1,N+1)]
used = [0] * N
p = [0] * R
f(0,N,R)