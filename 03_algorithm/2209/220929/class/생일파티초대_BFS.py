def bfs(N):
    q = [1] # 큐생성 + 시작점 인큐
    visited = [0] * (N+1)   # visited생성
    visited[1] = 1          # 시작점 방문 표시
    while q:                # 큐가 비어있지 않으면
        t = q.pop(0)
        if visited[t] > 3:
            break
        for i in range(1, N+1):
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1
    cnt = 0
    for i in range(1, N+1):
        if 1<visited[i]<4:
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int,input().split())
        adj[a][b] = 1
        adj[b][a] = 1
    result = bfs(1)
    print(f"#{tc} {result}")