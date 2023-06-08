from collections import deque
INF = 10**6
F, S, G, U, D = map(int,input().split())
queue = deque([S])
dp = [INF] * (F+1)
dp[S] = 0
while queue:
    now = queue.popleft()
    if now == G:
        break
    if now + U <= F:
        if dp[now+U] > dp[now] + 1:
            dp[now+U] = dp[now] + 1
            queue.append(now+U)
    if 0 < now - D:
        if dp[now-D] > dp[now] + 1:
            dp[now-D] = dp[now] + 1
            queue.append(now-D)

if dp[G] == INF:
    print("use the stairs")
else:
    print(dp[G])