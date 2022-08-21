n, m = map(int,input().split())
s = []
visited = [False] * n


def dfs(idx):
    if len(s) == m:
        print(*s)
        return

    for i in range(idx,n):
        if not visited[i]:
            visited[i] = True
            s.append(i+1)
            dfs(i+1)
            s.pop()
            visited[i] = False

dfs(0)