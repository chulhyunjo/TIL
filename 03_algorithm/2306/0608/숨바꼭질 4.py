from collections import deque

N, K = map(int, input().split())
if K < N:
    print(N-K)
    print(*list(range(N, K-1, -1)))
else:
    visited = [0] * ((K*2)+1)
    queue = deque([(N, 0, [N])])
    tmp = 0
    while queue:
        now, cnt, move = queue.popleft()
        if visited[now] == 1: continue
        visited[now] = 1
        if now == K:
            print(cnt)
            print(*move)
            break
        if now + 1 <= K:
            queue.append((now + 1, cnt + 1, move+[now+1]))
        if now - 1 >= 0:
            queue.append((now -1 , cnt + 1, move+[now-1]))
        if now * 2 < 2 * K - 1:
            queue.append((now*2, cnt + 1, move+[now*2]))
