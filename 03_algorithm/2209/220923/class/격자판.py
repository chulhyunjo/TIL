dx, dy =[1,-1,0,0], [0,0,1,-1]
def dfs(x,y,i,now):
    if i == 7:
        result.add(now)
        return
    else:
        for q in range(4):
            nx, ny = x + dx[q], y + dy[q]
            if 0 <= nx < 4 and 0 <= ny < 4:
                dfs(nx, ny, i+1, now+graph[nx][ny])


for tc in range(1,int(input())+1):
    graph = [list(input().split()) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,1,graph[i][j])
    print(f'#{tc} {len(result)}')