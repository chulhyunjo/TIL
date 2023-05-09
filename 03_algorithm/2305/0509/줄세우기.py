from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
nums = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    nums[b] += 1

queue = deque()
for i in range(1, N+1):
    if nums[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    print(x, end = " ")
    for i in graph[x]:
        nums[i] -= 1
        if nums[i] == 0:
            queue.appendleft(i)