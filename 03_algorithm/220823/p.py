def sheep(i, j):
    global w
    global s
    if arr[i][j] == 'v':
        w += 1
        visited[i][j] = 1
    else:
        visited[i][j] = 1
        if arr[i][j] == 'o':
            s += 1
        for k in range(4):
            ni = i + dy[k]
            nj = j + dx[k]
            if 0 <= ni < C and 0 <= nj < R and visited[ni][nj] == 0 and arr[ni][nj] != '#':
                sheep(ni, nj)

R, C = map(int, input().split())
arr = [list(input()) for _ in range(C)]
visited = [[0] * R for _ in range(C)]
S = W = 0
Si = []
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
s, w = -1, 0
for i in range(C):
    for j in range(R):
        if arr[i][j] == 'o':
            S += 1
            Si.append([i, j])
        elif arr[i][j] == 'v':
            W += 1
for i, j in Si:
    print('Si', i, j)
    sheep(i, j)
    if w >= s:
        S -= 1
    else:
        W -= (w / s)
    print('sw', s, w)
    s = w = 0
print(S, int(W))