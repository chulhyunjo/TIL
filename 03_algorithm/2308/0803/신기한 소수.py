import sys
sys.setrecursionlimit(10**5)

def isPrime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def dfs(x):
    for i in range(10):
        nx = x + str(i)
        if isPrime(int(nx)):
            if len(nx) == N:
                print(nx)
                continue
            dfs(nx)

N = int(input())
ans = 0
if N == 1:
    print(2,3,5,7, sep='\n')
else:
    for x in ['2','3','5','7']:
        dfs(x)