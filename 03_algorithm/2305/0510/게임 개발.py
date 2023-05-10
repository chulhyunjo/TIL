from collections import deque
import sys
input = sys.stdin.readline

queue = deque()
N = int(input())

buildings = [0] * (N+1)
times = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for k in range(1,N+1):
    T, *numbers = map(int, input().split())
    times[k] = T
    del numbers[-1]
    for i in numbers:
        graph[i].append(k)
        buildings[k] += 1

result = [0] * (N+1)
for i in range(1,N+1):
    if buildings[i] == 0:
        queue.append(i)
        result[i] += times[i]

while queue:
    now = queue.popleft()
    for i in graph[now]:
        result[i] = max(result[i], result[now] + times[i])
        buildings[i] -= 1
        if buildings[i] == 0:
            queue.append(i)

print(*result[1:], sep='\n')