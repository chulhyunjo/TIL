import sys
sys.setrecursionlimit(10**5)

# 각 칸에 들어 갈 수 있는 번호 return
def needNumber(x,y):
    used = [0] * 10
    # 가로, 세로 방향
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x+dx, y+dy
        while 0 <= nx < 9 and 0 <= ny < 9:
            now = board[nx][ny]
            if now != 0:
                used[now] = 1
            nx, ny = nx+dx, ny+dy
    # 3*3 모양 확인
    for i in range(x//3*3, x//3*3+3):
        for j in range(y//3*3, y//3*3 + 3):
            now = board[i][j]
            if now != 0:
                used[now] = 1
    # 가능한 숫자 배열 return
    return [i for i in range(1,10) if used[i] == 0]

# 현재 숫자가 가능한지 확인
def check(x, y, checknumber):
    # 가로 세로
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x+dx, y+dy
        while 0 <= nx < 9 and 0 <= ny < 9:
            now = board[nx][ny]
            # 현재 번호가 있다면 False
            if now == checknumber:
                return False
            nx, ny = nx+dx, ny+dy

    # 3*3모양 확인
    for i in range(x//3*3, x//3*3+3):
        for j in range(y//3*3, y//3*3 + 3):
            if i == x and j == y: continue
            now = board[i][j]
            # 현재 숫자가 있다면 false
            if now == checknumber:
                return False
    return True

# 하나씩 채우면서 백트래킹
def dfs(d):
    # 다 채웠으면 true return
    if d ==N:
        return True
    else:
        for i in numbers[d]:
            x, y = need[d]
            # 가능한지 여부 확인
            if check(x, y, i):
                # 가능하면 채우기
                board[x][y] = i
                if dfs(d+1): return True
                board[x][y] = 0
            else:
                continue


board = [list(map(int,input())) for _ in range(9)]

need = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            need.append((i,j))
N = len(need)

numbers = []
for x,y in need:
    numbers.append(needNumber(x,y))

dfs(0)
for i in range(9):
    print(*board[i], sep='')