from collections import deque

n = int(input())
arr = list(map(int,input().split()))

queue = deque(range(1,n+1))
result = []
while queue:
    x = queue.popleft()
    result.append(x)
    k = arr[x-1]
    if k > 0:
        queue.rotate(-(k-1))
    else:
        queue.rotate(-k)

print(*result)