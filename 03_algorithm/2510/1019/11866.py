from collections import deque

N, K = map(int, input().split())
queue = deque(range(1,N+1))

result = []
while queue:
    queue.rotate(-(K-1))
    result.append(queue.popleft())

result = "<" + ", ".join(map(str,result)) + ">"
print(result)