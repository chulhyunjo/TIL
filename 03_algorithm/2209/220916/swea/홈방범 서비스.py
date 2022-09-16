from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for tc in range(1,int(input())+1):
    n, m = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    result = 0
    for k in range(1,n+2):
        use = (k**2) + (k-1)**2
        for i in range(n):
            for j in range(n):
                visited = [[False] * n for _ in range(n)]
                visited[i][j] = True
                price = 0
                home = 0
                if graph[i][j] ==1:
                    price += m
                    home += 1
                queue = deque()
                queue.append((i,j,1))
                while queue:
                    x, y, cnt = queue.popleft()
                    if cnt == k: break
                    for q in range(4):
                        nx = x + dx[q]
                        ny = y + dy[q]
                        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                            if graph[nx][ny] == 1:
                                price += m
                                home += 1
                            queue.append((nx,ny,cnt +1))
                            visited[nx][ny] = True
                if price - use >= 0:
                    result = max(result, home)

    print(f'#{tc} {result}')