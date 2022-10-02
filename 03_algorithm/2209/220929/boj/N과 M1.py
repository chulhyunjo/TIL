def dfs(i,arr):
    if i == m:
        print(*arr)
    else:
        for q in range(1,n+1):
            dfs(i+1,arr+[q])


n, m = map(int,input().split())
used = [0] * (n+1)
dfs(0,[])