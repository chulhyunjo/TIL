from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수
q = PriorityQueue()
INF = 10**8
graph = [[] for _ in range(N+1)]

distance = [INF] * (N+1)
visited = [False] * (N+1)

for _ in range(M):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))

S, E = map(int,input().split())
distance[S] = 0
q.put((0,S))

while q.qsize() > 0:
    dis, now = q.get()
    if now == E: break
    if visited[now]: continue
    visited[now] = True
    for next,d in graph[now]:
        distance[next] = min(distance[next], dis + d)
        q.put((distance[next], next))

print(distance[E])