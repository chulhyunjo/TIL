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
    if x != y:
        parents[y] = x
        return True
    else:
        return False

V, E = map(int,input().split())
edge = []
for _ in range(E):
    a, b, c = map(int,input().split())
    heapq.heappush(edge, (c,a,b))

parents = list(range(V+1))
nodes = 0
answer = 0
while nodes < V-1:
    value, x, y = heapq.heappop(edge)
    if union(x,y):
        answer += value
        nodes += 1

print(answer)