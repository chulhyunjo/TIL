from collections import deque

def findCust(a,b):
    global oil, taxi_X, taxi_Y
    queue = deque()
    queue.append((a, b))
    visited = [[0] * n for _ in range(n)]
    find = n**2
    finded = []
    while queue:
        x, y = queue.popleft()
        if visited[x][y] > find: break
        if [x,y] in peopleStart:
            finded.append([x, y])
            find = visited[x][y]
        else:
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 > nx or 0 > ny or n <= nx or n <= ny: continue
                if visited[nx][ny] or graph[nx][ny] == 1: continue
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    if finded:
        finded.sort()
        dirx = finded[0][0]
        diry = finded[0][1]
        oil -= find
        idx = peopleStart.index([dirx, diry])
        gox, goy = peopleEnd[idx]
        need = goToDis(dirx, diry, gox, goy)
    else:
        return False

    if need == -1:
        return False
    else:
        taxi_X, taxi_Y = gox, goy
        peopleStart[idx] = [-1,-1]
        oil += need
        return True

def goToDis(a, b, gox, goy):
    queue = deque()
    queue.append((a,b))
    visited = [[0] * n for _ in range(n)]
    while queue:
        x, y = queue.popleft()
        if oil < visited[x][y] + 1: return -1
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 > nx or 0 > ny or n <= nx or n <= ny: continue
            if visited[nx][ny] or graph[nx][ny] == 1: continue
            if nx == gox and ny == goy:
                return visited[x][y]+1
            queue.append((nx,ny))
            visited[nx][ny] = visited[x][y] + 1
    return -1


n, m, oil = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
taxi_X, taxi_Y = map(int,input().split())
peopleStart = []
peopleEnd = []
for _ in range(m):
    x, y, dirx, diry = map(int,input().split())
    peopleStart.append([x-1,y-1])
    peopleEnd.append([dirx-1,diry-1])

taxi_X -= 1
taxi_Y -= 1
for _ in range(m):
    if not findCust(taxi_X,taxi_Y):
        oil = -1
        break
print(oil)
