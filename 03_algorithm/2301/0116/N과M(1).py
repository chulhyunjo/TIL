def dfs(cnt, result):
    if cnt == m:
        print(*result)
        return
    for i in range(n):
        if not use[i]:
            use[i] = 1
            dfs(cnt+1, result + [i+1])
            use[i] = 0

n, m = map(int,input().split())
use = [0] * n
dfs(0,[])