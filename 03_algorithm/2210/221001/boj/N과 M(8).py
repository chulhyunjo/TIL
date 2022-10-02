n, m = map(int, input().split())
num = sorted(map(int, input().split()))
result = [0] * m
def dfs(i, k):
    if i == m:
        print(*result)
    else:
        for j in range(k, n):
            result[i] = num[j]
            dfs(i + 1, j)
dfs(0, 0)