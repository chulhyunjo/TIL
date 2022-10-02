n, m = map(int,input().split())
result = [0] * m
num = sorted(map(int,input().split()))
d = dict()
def dfs(i):
    if i == m:
        if not d.get(tuple(result), 0):
            print(*result)
            d[tuple(result)] = 1
    else:
        for k in range(n):
            result[i] = num[k]
            dfs(i+1)
dfs(0)
