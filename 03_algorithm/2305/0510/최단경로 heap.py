import sys
input = sys.stdin.readline
from queue import PriorityQueue
INF = 10**7
V, E = map(int,input().split())
K = int(input())
dis = [INF] * (V+1)
graph = [[] for _ in range(V+1)]
q = PriorityQueue() # 우선순위 큐 -> 처음 써봄

for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))

q.put((0,K)) # 시작 지점 0은 거리
dis[K] = 0

visited = [False] * (V+1)
while q.qsize() > 0: # 우선 순위 큐에 있는 동안
    now = q.get() # 꺼내기
    c_v = now[1] # 위치
    if visited[c_v]:
        continue
    visited[c_v] = True
    for tmp in graph[c_v]:
        next = tmp[0]
        value = tmp[1]
        if dis[next] > dis[c_v] + value: # 최소 거리로 업데이트
            dis[next] = dis[c_v] + value
            # 가중치가 정렬 기준이므로 순서를 가중치, 목표 노드 순으로 우선순위 큐에 넣기
            q.put((dis[next], next))

for i in range(1, V+1):
    if visited[i]:
        print(dis[i])
    else:
        print("INF")
