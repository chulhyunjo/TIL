R, C, T = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(R)]

def findDust():
    dusts = []
    for i in range(R):
        for j in range(C):
            if room[i][j] >=5:
                dusts.append((i,j,room[i][j]))
    return dusts


def dustTime():
    dusts = findDust()
    for dust in dusts:
        x, y, nums = dust
        cnt = 0
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 > nx or 0 > ny or R <= nx or C <= ny: continue
            if room[nx][ny] == -1: continue
            room[nx][ny] += nums // 5
            cnt += 1
        room[x][y] -= (nums // 5) * cnt

def airTime(pos, x, y):
    global totalNum
    positionx, positiony = x, y
    if pos == 1:
        d = [(-1,0), (0,1), (1,0), (0,-1)]
        m = 0
        while m < 4:
            dx, dy = d[m]
            if 0 <= x + dx <= positionx  and 0 <= y + dy < C:
                x, y = x + dx, y + dy
                if room[x][y] > 0:
                    if room[x - dx][y - dy] == -1:
                        totalNum -= room[x][y]
                        room[x][y] = 0
                    else:
                        room[x - dx][y - dy] = room[x][y]
                        room[x][y] = 0
            else: m += 1
    if pos == -1:
        d = [(1,0), (0,1), (-1,0), (0,-1)]
        m = 0
        while m < 4:
            dx, dy = d[m]
            if positionx <= x + dx < R and 0 <= y + dy < C:
                x, y = x + dx, y + dy
                if room[x][y] > 0:
                    if room[x - dx][y - dy] == -1:
                        totalNum -= room[x][y]
                        room[x][y] = 0
                    else:
                        room[x - dx][y - dy] = room[x][y]
                        room[x][y] = 0
            else:
                m += 1


airTopX = airTopY = 0
airBottomX = airBottomY = 0
totalNum = 0
tmp = 0
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            if not tmp:
                airTopX, airTopY = (i,j)
                tmp = 1
            else:
                airBottomX, airBottomY = (i,j)
        else:
            totalNum += room[i][j]

for _ in range(T):
    dustTime()
    airTime(1, airTopX, airTopY)
    airTime(-1, airBottomX, airBottomY)

print(totalNum)