import heapq
import sys
input = sys.stdin.readline


def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]


def union(x,y):
    x = find(x)
    y = find(y)
    if x > y:
        x, y = y, x
    if x != y:
        parents[y] = x
        return True
    else:
        return False

N, M = map(int,input().split())
parents = [i for i in range(N+1)]
position = [(0,0) for _ in range(N+1)]
pq = []

for i in range(1,N+1):
    a, b = map(int,input().split())
    position[i] = (a,b)

for j in range(M):
    a, b = map(int,input().split())
    union(a,b)

for i in range(1,N):
    for j in range(i+1, N+1):
        x1, y1 = position[i]
        x2, y2 = position[j]
        distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
        heapq.heappush(pq, (distance, i,j))

answer = 0
while pq:
    dis, a, b = heapq.heappop(pq)
    if union(a,b):
        answer += dis

print("%.2f" %(answer))