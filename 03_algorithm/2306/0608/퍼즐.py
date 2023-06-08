from collections import deque
dx, dy = [1,0,-1,0], [0,1,0,-1]

def strToArr(s):
    arr = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            arr[i][j] = s[3*i + j]
    return arr

def arrToStr(arr):
    nums = ''
    for i in range(3):
        for j in range(3):
            nums += str(arr[i][j])
    return nums

check = dict()
FINISH = '123456780'
graph = [list(map(int,input().split())) for _ in range(3)]

queue = deque()
first = arrToStr(graph)
queue.append((first,0))
check[first] = 1
answer = -1
while queue:
    now, cnt = queue.popleft()

    if now == FINISH:
        answer = cnt
        break
    arr = strToArr(now)
    x = y = 0
    for i in range(9):
        if now[i] == '0':
            x = i // 3
            y = i % 3
            break
    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]
        if 0<=nx<3 and 0<=ny<3:
            arr[nx][ny], arr[x][y] = arr[x][y], arr[nx][ny]
            nxt = arrToStr(arr)
            if check.get(nxt, 0):
                arr[nx][ny], arr[x][y] = arr[x][y], arr[nx][ny]
                continue
            check[nxt] = 1
            queue.append((nxt, cnt + 1))
            arr[nx][ny], arr[x][y] = arr[x][y], arr[nx][ny]

print(answer)