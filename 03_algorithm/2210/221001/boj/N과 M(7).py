n, m = map(int, input().split())
num = sorted(map(int, input().split()))
result = [0] * m
def dfs(i):
    if i == m:
        print(*result)
    else:
        for j in range(n):
            result[i] = num[j]
            dfs(i + 1)
dfs(0)