from collections import deque

n, k, m = map(int,input().split())
queue = deque(range(1, n+1))
tmp = k-1
cnt = 0
while queue:
    if cnt and not cnt % m:
        if tmp == k-1:
            tmp = -k
        else:
            tmp = k-1
        queue.rotate(-tmp)
        print(queue.popleft())
        cnt = 0

    else:
        queue.rotate(-tmp)
        print(queue.popleft())
    cnt += 1