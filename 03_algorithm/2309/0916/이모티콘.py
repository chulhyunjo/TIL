from collections import deque

def bfs():
    queue = deque([(1,0)])
    while queue:
        cnt, clip = queue.popleft()
        if clip == S:
            return visited[cnt][clip]
        # 1번 연산
        if visited[cnt][cnt] == -1:
            queue.append((cnt, cnt))
            visited[cnt][cnt] = visited[cnt][clip] + 1
            printed[cnt] = 1
        # 2번 연산
        if cnt + clip<=S and visited[cnt + clip][clip] == -1:
            queue.append((cnt + clip, clip))
            visited[cnt+clip][clip] = visited[cnt][clip] + 1
        # 3번 연산
        if cnt > 1 and visited[cnt-1][clip] == -1:
            queue.append((cnt-1, clip))
            visited[cnt-1][clip] = visited[cnt][clip] + 1

INF = int(10**6)
S = int(input())
visited =[[-1] *(S+1) for _ in range(S+1)]

printed = [0] * (S+1)
print(bfs())