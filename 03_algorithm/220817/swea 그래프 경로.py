def dfs(start):
    visited[start] = True
    result.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

for tc in range(1, int(input())+1):
    v, e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    result = []
    for _ in range(e):
        a, b = map(int,input().split())
        graph[a].append(b)

    s, g = map(int,input().split())
    dfs(s)
    if g in result:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')