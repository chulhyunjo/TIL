def dfs(x,y,d):
    global answer
    if d == M:
        answer += 1
        return
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x + dx, y + dy
        if 0 > nx or N <= nx or 0 > ny or N <= ny: continue
        if visited[nx][ny] or graph[nx][ny] == 1: continue
        m = moves_dict.get((nx,ny), -1)
        if m == -1:
            visited[nx][ny] = True
            dfs(nx, ny, d)
            visited[nx][ny] = False
        elif m == d:
            visited[nx][ny] = True
            dfs(nx, ny, d+1)
            visited[nx][ny] = False
#
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

moves_dict = dict()
moves = []

for i in range(M):
    x, y = map(lambda x: int(x) - 1, input().split())
    moves.append((x,y))
    moves_dict[(x,y)] = i

visited = [[False] * N for _ in range(N)]
first_x, first_y = moves[0]
visited[first_x][first_y] = True
answer = 0

dfs(first_x, first_y, 1)
print(answer)