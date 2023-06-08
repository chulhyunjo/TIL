N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = list(map(int,input().split())) + [0]
s = answer[0]
idx = 1
visited = [False] * (N+1)
visited[s] = True

def dfs(x):
    global idx
    if idx == N:
        return True
    nxt = answer[idx]
    if nxt in graph[x]:
        idx += 1
        if dfs(nxt):
            return True
        else:
            if answer[idx] in graph[x]:
                idx += 1
                if dfs(answer[idx]):
                    return True
                else:
                    return False
            else: return False
    else:
        return False

if dfs(s): print(1)
else: print(0)




