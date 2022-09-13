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


t = int(input())
for _ in range(t):
    n = int(input())
    while True:
        if isPrime(n):
            print(n)
            break
        n += 1