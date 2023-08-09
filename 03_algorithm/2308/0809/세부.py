import heapq
import sys
input = sys.stdin.readline

def bfs():
    while pq:
        k, x = heapq.heappop(pq)
        # 현재 무게제한이 탐색하고자하는 무게제한 보다 클 경우 생략
        if cost[x] > -k:
            continue
        for nx, nk in graph[x]:
            # 다음 이동할 때 가격 (무게 제한이 낮은 만큼)
            nxt = min(nk, -k)
            # 다음 이동칸이 무게 제한이 더 낮은 경우 큰걸로 갱신
            if cost[nx] < nxt:
                heapq.heappush(pq, (-nxt, nx))
                cost[nx] = nxt

N, M = map(int,input().split())
s, e = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    h1, h2, k = map(int,input().split())
    graph[h1].append((h2, k))
    graph[h2].append((h1, k))

# 최대 힙
pq = [(-10**6-1,s)]

# 각 노드별 들고 갈 수 있는 개수
cost = [0] * (N+1)
cost[s] = 10**6+1

bfs()
print(cost[e])