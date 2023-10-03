def checkBlank(x, y):
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x + dx, y + dy
        if 0>nx or 0>ny or N<=nx or N<=ny: continue
        if not graph[nx][ny]:
            blanks[x][y] += 1


def findMost(x, y):
    most = 0
    position = (-1,-1)
    for dx, dy in [(-1,0),(0,-1),(0,1),(1,0)]:
        nx, ny = x + dx, y + dy
        if 0 > nx or 0 > ny or N <= nx or N <= ny: continue


    return position

N = int(input())

graph = [[0]*N for _ in range(N)]
blanks = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        checkBlank(i,j)

likes = dict()
order = []
sitDown = dict()

for _ in range(N**2):
    a, *like = map(int,input().split())
    likes[a] = like
    order.append(a)

for num in order:
    flag = 0
    for like in likes[num]:
        if sitDown.get(like, 0):
            x, y = sitDown[like]
            px, py = findMost(x, y)
            if px != -1 and py != -1:
                flag = 1



    if not flag:
        max_blank = 0
        sit = (-1, -1)
        for i in range(N):
            for j in range(N):
                if blanks[i][j] > max_blank:
                    max_blank = blanks[i][j]
                    sit = (i, j)
        x, y = sit
        sitDown[num] = (x, y)
        blanks[x][y] = 0

print(*blanks, sep='\n')
