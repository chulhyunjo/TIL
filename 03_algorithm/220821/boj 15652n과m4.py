n, m = map(int,input().split())
visited = [False] * n
s = []


def dfs(idx):
    if len(s) == m:
        print(*s)
        return

    for i in range(idx,n):
        s.append(i+1)
        dfs(i)
        s.pop()

dfs(0)