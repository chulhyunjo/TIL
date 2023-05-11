import sys
input = sys.stdin.readline

INF = 10 ** 9
N, M = map(int,input().rstrip().split())
edges = []
dis = [INF] * (N+1)
dis[1] = 0 # 출발 도시

for _ in range(M):
    A, B, C = map(int,input().rstrip().split())
    edges.append((A,B,C))

for _ in range(N-1):
    for start, end, time in edges:
        if dis[start] != INF and dis[end] > dis[start] + time:
            dis[end] = dis[start] + time

mCycle = False

for start, end, time in edges:
    if dis[start] != INF and dis[end] > dis[start] + time:
        mCycle = True

if not mCycle:
    for i in range(2, N+1):
        if dis[i] != INF:
            print(dis[i])
        else:
            print(-1)
else:
    print(-1)