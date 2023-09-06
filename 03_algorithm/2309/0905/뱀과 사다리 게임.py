from collections import deque

def bfs():
    queue = deque([(1,0)])
    while queue:
        now, cnt = queue.popleft()
        for i in range(1, 7):
            if visited[now + i]: continue
            if now + i == 100:
                return cnt + 1
            if board[now + i]:
                queue.append((board[now+i], cnt + 1))
                visited[now+i] = 1
            else:
                queue.append((now+i, cnt + 1))
                visited[now+i] = 1

N, M = map(int,input().split())
board = [0] * 101
visited = [0] * 101
visited[1] = 1
for _ in range(N+M):
    x, y = map(int,input().split())
    board[x] = y

answer = bfs()
print(answer)