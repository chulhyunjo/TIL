def isPrime(x):
    if x == 1: return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

N = int(input())

while True:
    if str(N) == str(N)[::-1]:
        if isPrime(N):
            print(N)
            break
    N += 1