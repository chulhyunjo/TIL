n, m = map(int,input().split())
num = sorted(map(int,input().split()))
result = [0] * m

def dfs(i, j):
    if i == m:
        print(*result)
    else:
        if j < n:
            result[i] = num[j]
            dfs(i+1, j+1)

            result[i] = 0
            dfs(i, j+1)
dfs(0,0)