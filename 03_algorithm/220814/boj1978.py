def isPrime(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n % 2 == 0:
        return 0
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                return 0
            i += 1
        return 1

n = int(input())
arr = list(map(int,input().split()))
cnt = 0
for i in arr:
    if isPrime(i):
        cnt += 1
print(cnt)