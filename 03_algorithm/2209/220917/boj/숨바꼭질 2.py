from collections import deque

N, K = map(int,input().split())
queue = deque()
queue.append((N,0))
result = 0
result_time = int(1e5)
v = [1] * 100001
while queue:
    n, cnt = queue.popleft()
    v[n] = 0
    if cnt > result_time:
        break
    if n == K:
        result += 1
        result_time = cnt
    if n+1 <= 100000 and v[n+1]:
        queue.append((n+1,cnt+1))
    if 0 <= n-1 and v[n-1]:
        queue.append((n-1,cnt+1))
    if 2*n <= 100000 and v[2*n]:
        queue.append((2*n,cnt+1))
print(result_time, result, sep='\n')