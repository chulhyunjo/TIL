import sys
sys.setrecursionlimit(10**6)
def dfs(s):
    v[s] = 1
    for w in sorted(graph[s]):
        cnt = 1
        if v[w] == 0:
            cnt = cnt + dfs(w)
            v[w] = 0
            return cnt
    return 0
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n):              #시작 위치에 따라
    v = [0]*n
    if dfs(i) >= 4:
        print(1)
        break
else:
    print(0)