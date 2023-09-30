D = [(-1,0),(0,1),(1,0),(0,-1)] # 북, 동, 남, 서

N, M = map(int,input().split())
r, c, d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

def findSpace(r, c):
    for dx, dy in D:
        nr, nc = r + dx, c + dy
        if graph[nr][nc] == 0:
            return True
    return False

def moveBack(r, c, d):
    dx, dy = D[(d+2) % 4]
    nr, nc = r + dx, c + dy
    if graph[nr][nc] == 1:
        return (-1,-1)
    else:
        return (nr, nc)


def moveFront(r, c, d):
    dx, dy = D[d]
    nr, nc = r + dx, c + dy
    if graph[nr][nc] == 0:
        return (nr, nc)
    else:
        return (-1, -1)


answer = 1
while True:
    graph[r][c] = 2 # 청소

    if findSpace(r, c): # 현재 칸에서 빈칸 찾기 -> True면 있다는 거
        d = (d+3) % 4
        nr, nc = moveFront(r, c, d)
        while nr == -1 and nc == -1:
            d = (d+3) % 4
            nr, nc = moveFront(r,c,d)
        r, c = nr, nc
        answer += 1
    else:
        r, c = moveBack(r, c, d)
        if r == -1 and c == -1:
            break

print(answer)