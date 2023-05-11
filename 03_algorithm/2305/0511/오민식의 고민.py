import sys
input = sys.stdin.readline
INF = 1e11
N, S, E, M = map(int,input().split())
edges = []
result = [-INF] * N

for _ in range(M):
    u, v, w = map(int,input().split())
    edges.append((u,v,-w))

getMoney = list(map(int,input().split()))
result[S] = getMoney[S]
for _ in range(N):
    for edge in edges:
        u,v,w = edge
        if result[u] == -INF:
            continue
        elif result[v] < result[u] + w + getMoney[v]:
            result[v] = result[u] + w + getMoney[v]

for _ in range(100):
    for edge in edges:
        u,v,w = edge
        if result[u] == INF:
            result[v] = INF
        elif result[u] == -INF:
            continue
        elif result[v] < result[u] + w + getMoney[v]:
            result[v] = INF
            break

if result[E] == -INF:
    print("gg")
elif result[E] == INF:
    print("Gee")
else:
    print(result[E])