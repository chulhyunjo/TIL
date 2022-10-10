def find_top(y, g):
    x = 0
    while x < h:
        if g[x][y] != 0:
            return x
        x += 1
    return -1


def combination(d):
    global maxV, total_cnt
    if total_cnt - maxV == 0: return
    if d == n:
        maxV = max(maxV, playGame())
        return
    else:
        for i in range(w):
            order[d] = i
            combination(d + 1)


def bomb(x, y, cnt, g):
    ct = 0
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        for m in range(1, cnt):
            nx, ny = x + dx * m, y + dy * m
            if 0 > nx or 0 > ny or h <= nx or w <= ny: continue
            if g[nx][ny] > 1:
                bombArea.append((nx, ny, g[nx][ny]))
            if g[nx][ny] != 0:
                g[nx][ny] = 0
                ct += 1
    return ct


def playGame():
    playGraph = [graph[i][:] for i in range(h)]
    t = 0
    result = 0
    while t < n:
        now = find_top(order[t], playGraph)
        if now == -1:
            t += 1
            continue

        if playGraph[now][order[t]] == 1:
            playGraph[now][order[t]] = 0
            result += 1
        else:
            bombArea.append((now, order[t], playGraph[now][order[t]]))
            playGraph[now][order[t]] = 0
            result += 1
            while bombArea:
                x, y, cnt = bombArea.pop()
                result += bomb(x, y, cnt, playGraph)

            for j in range(w):
                for i in range(h - 1, -1, -1):
                    if playGraph[i][j] != 0:
                        nx = i + 1
                        while 0 < nx < h and playGraph[nx][j] == 0:
                            nx += 1
                        playGraph[i][j], playGraph[nx - 1][j] = 0, playGraph[i][j]
        t += 1
    return result


for tc in range(1, int(input()) + 1):
    n, w, h = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(h)]

    total_cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] != 0:
                total_cnt += 1

    order = [0] * n
    bombArea = []
    maxV = 0
    combination(0)
    print(f'#{tc} {total_cnt - maxV}')
