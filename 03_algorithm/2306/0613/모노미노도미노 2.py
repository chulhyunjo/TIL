board = [[0] * 10 for _ in range(10)]

def putBlock(x, y, t):
    nx = x + (3-x)
    ny = y + (3-y)
    tmp = 0
    if t == 1:
        while nx < 9:
            if board[nx+1][y] == 1:
                break
            nx += 1
        while ny < 9:
            if board[x][ny+1]:
                break
            ny += 1
    elif t == 2:
        while nx < 9:
            if board[nx+1][y] or board[nx+1][y+1]:
                break
            nx += 1
        while ny < 9:
            if board[x][ny+1]:
                break
            ny += 1
        board[nx][y+1] = 1
        board[x][ny-1] = 1
        if ny - 1 < 6:
            tmp = 1
    else:
        while nx < 9:
            if board[nx+1][y] == 1:
                break
            nx += 1
        while ny < 9:
            if board[x][ny+1] or board[x+1][ny+1]:
                break
            ny += 1
        board[nx-1][y] = 1
        board[x+1][ny] = 1
        if nx - 1 < 6:
            tmp = 2
    board[x][ny] = 1
    board[nx][y] = 1
    g = check('g')
    b = check('b')
    if nx == 5 and not g:
        goDown('g', 9, 0)
    if ny == 5 and not b:
        goDown('b', 9, 0)
    if tmp == 1:
        if ny - 1 == 5 and not b:
            goDown('b', 9, 0)
        if ny - 1 == 4 and b <= 1:
            goDown('b', 9, 0)
    elif tmp == 2:
        if nx - 1 == 5 and not g:
            goDown('g', 9, 0)
        if nx - 1 == 4 and g <= 1:
            goDown('g', 9, 0)

def check(g_b):
    idx = 9
    flag = 0
    if g_b == 'g':
        while idx >= 6:
            cnt = 0
            for j in range(4):
                if board[idx][j] == 1:
                    cnt += 1
                else:
                    idx -= 1
                    break
            else:
                goDown(g_b, idx, 1)
                flag += 1
    if g_b == 'b':
        while idx >= 6:
            cnt = 0
            for j in range(4):
                if board[j][idx] == 1:
                    cnt += 1
                else:
                    idx -= 1
                    break
            else:
                goDown(g_b, idx, 1)
                flag += 1
    return flag

def goDown(g_b,idx, score):
    global answer
    answer += score
    if g_b == 'g':
        for i in range(idx, 4, -1):
            for j in range(4):
                board[i][j] = board[i-1][j]
                board[i - 1][j] = 0
    if g_b == 'b':
        for i in range(idx, 4, -1):
            for j in range(4):
                board[j][i] = board[j][i-1]
                board[j][i - 1] = 0


N = int(input())
answer = 0
answercnt = 0

for _ in range(N):
    t, x, y = map(int,input().split())
    putBlock(x, y, t)

for i in range(6, 10):
    for j in range(4):
        if board[i][j]: answercnt += 1
        if board[j][i]: answercnt += 1

print(answer)
print(answercnt)