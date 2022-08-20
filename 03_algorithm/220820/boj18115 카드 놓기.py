from collections import deque

n = int(input())
arr = list(map(int,input().split()))
queue = deque()
arr.reverse()
for i in range(1,n+1):
    if arr[i-1] == 1:
        queue.appendleft(i)
    if arr[i-1] == 2:
        queue.insert(1, i)
    if arr[i-1] == 3:
        queue.append(i)
print(*queue)