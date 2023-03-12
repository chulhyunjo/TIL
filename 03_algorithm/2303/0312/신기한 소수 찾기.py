import sys
sys.setrecursionlimit(10**6)

def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    else:
        return True

def dfs(d, now):
    if d == n:
        if isPrime(int(now)):
            print(now)
    elif d < n:
        for i in odd:
            if isPrime(int(now+i)):
                dfs(d+1, now+i)


prime = ['2', '3', '5', '7']
n = int(input())
odd = ['1','3','5','7','9']

for i in prime:
    dfs(1,i)
