from collections import deque
N, L = map(int,input().split())
nums = list(map(int,input().split()))

queue = deque()
for i in range(N):
    while queue and queue[-1][0] > nums[i]:
        queue.pop()

    queue.append((nums[i],i))

    if i - queue[0][1] >= L:
        queue.popleft()

    print(queue[0][0], end=' ')