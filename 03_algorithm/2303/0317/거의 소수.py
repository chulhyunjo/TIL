def eratos(a,b):
    numbers = [True] * (int(b**0.5)+1)
    numbers[0] = numbers[1] = False
    for i in range(2, int((int(b**0.5)+1)**0.5)+1):
        if numbers[i] == True:
            for j in range(2*i, int(b**0.5)+1, i):
                numbers[j] = False
    return [k for k in range(2,int(b**0.5)+1) if numbers[k]==True]

a, b = map(int,input().split())
primeNum = eratos(a,b)
result = set()
for i in primeNum:
    n = 2
    while i**n <= b:
        if (i**n) >= a:
            result.add(i**n)
        n += 1

print(len(result))
