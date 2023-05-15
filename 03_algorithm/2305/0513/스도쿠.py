import sys
sys.setrecursionlimit(10**5)


def check_square(x, y, arr):
    start_x = (x//3)*3
    start_y = (y//3)*3
    for i in range(start_x, start_x+3):
        for j in range(start_y, start_y+3):
            arr[graph[i][j]] = 1


def check_row(x, arr):
    for i in range(9):
        arr[graph[x][i]] = 1


def check_col(y, arr):
    for i in range(9):
        arr[graph[i][y]] = 1


graph = [list(map(int,input().split())) for _ in range(9)]

zero_place = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zero_place.append((i,j))
need_place = len(zero_place)


def backtracking(d):
    available = [0] * 10
    if d == need_place:
        return True
    x, y = zero_place[d]
    check_square(x, y, available)
    check_col(y, available)
    check_row(x, available)
    for i in range(1,10):
        if available[i] == 0:
            graph[x][y] = i
            if backtracking(d+1):
                return True
            graph[x][y] = 0
    else:
        return False


backtracking(0)
for i in range(9):
    print(*graph[i])