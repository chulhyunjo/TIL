from collections import deque

N, K = map(int,input().split())
queue = deque()
queue.append((N,0))
v = [1] * 100001
while True:
    n, cnt = queue.popleft()
    if n == K:
        print(cnt)
        exit()
    if n+1 <= 100000 and v[n+1]:
        queue.append((n+1,cnt+1))
        v[n+1] = 0
    if 0 <= n-1 and v[n-1]:
        queue.append((n-1,cnt+1))
        v[n-1] = 0
    if 2*n <= 100000 and v[2*n]:
        queue.append((2*n,cnt+1))
        v[2*n] = 0