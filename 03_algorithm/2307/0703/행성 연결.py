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
    return False


N = int(input())
parents = [i for i in range(N)]
graph = [list(map(int,input().split())) for _ in range(N)]
info = []
for i in range(N):
    for j in range(i+1, N):
        heapq.heappush(info, (graph[i][j], i, j))

answer = 0
cnt = 0
while cnt < N-1:
    cost, a, b = heapq.heappop(info)
    if union(a, b):
        cnt += 1
        answer += cost

print(answer)