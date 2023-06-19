import sys

input = sys.stdin.readline

N, K = map(int, input().split())


def dfs(d, max_x, max_y, min_x, min_y, area):
    global answer
    if d == K + 1:
        answer = min(area, answer)
        return
    dotnums = len(dots[d])
    for j in range(dotnums):
        x, y = dots[d][j]
        if min_x < x < max_x and min_y < y < max_y:
            dfs(d + 1, max_x, max_y, min_x, min_y, area)
        else:
            tmp_x1 = max(max_x, x)
            tmp_x2 = min(min_x, x)
            tmp_y1 = max(max_y, y)
            tmp_y2 = min(min_y, y)

            nxt_area = (tmp_x1 - tmp_x2) * (tmp_y1 - tmp_y2)
            if nxt_area >= answer: continue
            dfs(d + 1, tmp_x1, tmp_y1, tmp_x2, tmp_y2, nxt_area)


dots = [[] for _ in range(K + 1)]
for _ in range(N):
    x, y, k = map(int, input().split())
    dots[k].append((x, y))
    dots[k].sort()

answer = int(4e6)
dotsnum = len(dots[1])
for i in range(dotsnum):
    x, y = dots[1][i]
    dfs(2, x, y, x, y, 0)
print(answer)