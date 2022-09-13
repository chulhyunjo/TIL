from collections import deque

n, m = map(int,input().split())
arr = list(map(int,input().split()))
queue = deque(range(1,n+1))

cnt = 0
i = 0

while True:
    while i < m and arr[i] == queue[0]:
        queue.popleft()
        i += 1

    if i == m:
        break

    findIdx = queue.index(arr[i])
    if findIdx < (len(queue)) - findIdx:
        queue.rotate(-findIdx)
        cnt += findIdx

    else:
        queue.rotate((len(queue))-findIdx)
        cnt += len(queue) - findIdx

    queue.popleft()
    i += 1
print(cnt)