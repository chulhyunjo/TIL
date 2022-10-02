n, m = map(int,input().split())

def dfs(i, j, r):
    if i == m:
        print(*r)
    else:
        for k in range(j, n+1):
            dfs(i+1, k,r+[k])

dfs(0, 1, [])