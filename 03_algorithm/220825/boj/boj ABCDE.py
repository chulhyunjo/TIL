import sys
input = sys.stdin.readline

def dfs(x,cnt):
    global result
    if cnt == 4:
        result += 1
        return
    visited[x] = True
    for j in sorted(graph[x]):
        if not visited[j]:
            dfs(j,cnt+1)
            visited[j] = False


n, m = map(int,input().rstrip().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
for i in range(n):
    visited = [False] * n
    cnt = 0
    dfs(i,cnt)
    if result:
        break
if result:
    print(1)
else:
    print(0)
