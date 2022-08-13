def isPrime(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        i = 2
        while i ** 2 <= n:
            if n % i == 0:
                return 0
            i += 1
        return 1


m = int(input())
n = int(input())

sum1 = 0
minnum = n
for i in range(m, n+1):
    if isPrime(i):
        sum1 += i
        minnum = i if minnum > i else minnum

if sum1 == 0 :
    print(-1)
else:
    print(sum1)
    print(minnum)