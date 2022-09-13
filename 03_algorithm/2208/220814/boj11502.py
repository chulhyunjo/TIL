import sys
input = sys.stdin.readline

def isPrime(a):
    if a == 1 or a == 0:
        return False
    else:
        for i in range(2, int(a**0.5)+1):
            if a % i == 0:
                return False
            i += 1
        return True

def findSum(a):
    for i in arr:
        for j in arr:
            for k in arr:
                if i + j + k == a:
                    return f'{i} {j} {k}'
    return 0

arr = []
for i in range(2,1001):
    if isPrime(i):
        arr.append(i)

for _ in range(int(input())):
    k = int(input())
    print(findSum(k))