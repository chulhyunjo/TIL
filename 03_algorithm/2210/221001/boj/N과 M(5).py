n, m = map(int,input().split())
result = [0] * m
num = sorted(map(int,input().split()))
used = [0] * n

def dfs(i):
    if i == m:
        print(*result)
    else:
        for j in range(n):
            if not used[j]:
                used[j] = 1
                result[i] = num[j]
                dfs(i+1)
                result[i] = 0
                used[j] = 0
dfs(0)