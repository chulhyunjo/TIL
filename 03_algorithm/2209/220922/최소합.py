dx = [0,1]
dy = [1,0]

def minValue(x,y,s):
    global minV
    if (x,y) == (n-1, n-1):
        if s < minV:
            minV = s
    if s > minV:
        return

    else:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <n and ny < n:
                minValue(nx,ny,s+graph[nx][ny])


for tc in range(1, int(input())+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    minV = int(1e9)
    minValue(0,0,graph[0][0])
    print(f'#{tc} {minV}')
