n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
moved = [[0] * n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

move = 0
i = j = 0

for _ in range((n*n)-1):
    minI = i
    minJ = j

    moved[i][j] = 1
    moving = moved[:]
    for a in range(n):
        for b in range(n):
            if arr[minI][minJ] > arr[a][b] and moving[a][b] == 0:
                minI, minJ = a, b
    arr[i][j], arr[minI][minJ] = arr[minI][minJ], arr[i][j]

    ni = i + dx[move]
    nj = j + dy[move]

    if 0 <= ni < n and 0 <= nj < n and moved[ni][nj] == 0:
        i, j = ni, nj
    else:
        move = (move + 1) % 4
        i, j = i + dx[move], j + dy[move]

for i in arr:
    print(*i)