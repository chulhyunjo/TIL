def eratos(n):
    numbers = [True] * (10**7 +1)
    numbers[0] = numbers[1] = False
    for i in range(2, int((10**7)**0.5)+1):
        if numbers[i] == True:
            for j in range(2*i, 10**7+1, i):
                numbers[j] = False
    return [k for k in range(n, 10**7+1) if numbers[k]==True]


n = int(input())
primenum = eratos(n)
for k in primenum:
    if str(k) == str(k)[::-1]:
        print(k)
        break
