def eratos(a,b):
    arr = [True] * (b+1)
    arr[0] = arr[1] = False

    for i in range(2, int(b**0.5)+1):
        if arr[i] == True:
            for j in range(i+i, b+1, i):
                arr[j] = False
    return [k for k in range(a, b+1) if arr[k] == True]

m, n = map(int, input().split())
for i in eratos(m,n):
    print(i)