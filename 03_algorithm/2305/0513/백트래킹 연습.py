n, m =map(int,input().split())

nums = list(range(1,n+1))
visited = [0] * (n+1)


def dfs(d,lst):
    if d == m:
        print(*lst)
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            dfs(d+1, lst + [i])
            visited[i] = False

dfs(0,[])