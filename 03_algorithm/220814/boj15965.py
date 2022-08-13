def eratos(n):
    arr = [True] * (n+1)
    arr[0] = arr[1] = False

    for i in range(2, int(n**0.5)+1):
        if arr[i] == True:
            for j in range(i+i, n+1, i):
                arr[j] = False
    return [k for k in range(n+1) if arr[k] == True]

arr = eratos(7368791)
k = int(input())
print(arr[k-1])