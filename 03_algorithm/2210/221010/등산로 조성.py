def findhighest(height):
    highestIdx = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == height:
                highestIdx.append((i, j))
    return highestIdx
def find(x,y):
    queue = [(x,y,1)]
    while queue:
        x, y, cnt = queue.pop(0)
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 > nx or 0 > ny or n <= nx or n <= ny: continue
            if graph[x][y] > graph[nx][ny]:
                queue.append((nx,ny,cnt+1))
    return cnt


for tc in range(1,int(input())+1):
    n, k = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    result = 0

    topmost = max(map(max,*graph))
    highestIdx = findhighest(topmost)
    for i in range(n):
        for j in range(n):
            t = 0
            while t <= k:
                for x, y in highestIdx:
                    if graph[x][y] == topmost:
                        result = max(find(x,y), result)
                graph[i][j] -= 1
                t += 1
            graph[i][j] += (k+1)
    print(f'#{tc} {result}')