def makeBlock(x, d):
    # 벽 3개 세우면 검사
    if d == 3:
        if check():
            return True
        return False

    for i in range(x, N**2):
        if graph[i // N][i % N] == 'X':
            graph[i // N][i % N] = 'O'
            if makeBlock(i+1, d+1):
                return True
            graph[i // N][i % N] = 'X'
    return False


def check():
    for x, y in teachers:
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx, ny = x+dx, y+dy
            while 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 'O':
                    break
                if graph[nx][ny] == 'S':
                    return False
                nx += dx
                ny += dy
    return True


N = int(input())
graph = [list(input().split()) for _ in range(N)]

teachers = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'T':
            teachers.append((i,j))

if makeBlock(0,0):
    print('YES')
else:
    print('NO')
