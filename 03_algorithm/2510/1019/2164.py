from collections import deque

N = int(input())

queue = deque(range(1, N+1))
for _ in range(N-1):
    queue.popleft()
    queue.rotate(-1)

print(queue[0])