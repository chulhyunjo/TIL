def eratos(m, n):
    numbers = [True] * (n+1)
    numbers[0] = numbers[1] = False
    for i in range(2, int(n**(1/2))+1):
        if numbers[i] == True:
            for j in range(2*i, n+1, i):
                numbers[j] = False

    return [k for k in range(m,n+1) if numbers[k] == True]

m, n = map(int,input().split())
result = eratos(m,n)
print(*result, sep="\n")
