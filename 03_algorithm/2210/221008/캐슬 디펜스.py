dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

N, M, D = map(int,input().split())
graph = []
for _ in range(N):
    graph += list(map(int,input().split()))
graph += [0]*M
totalZombie = 0
for i in range(N):
    for j in range(M):
        if graph[i*M + j] == 1:
            totalZombie += 1

def put_archer(d, y):
    if d == 3:
        playGame()
        return
    for i in range(y+1, M):
        graph[N*M + i] = 2
        put_archer(d+1, i)
        graph[N*M + i] = 0

def playGame():
    global maxV
    v = graph[::]
    archer = []
    result = 0
    nowZombie = totalZombie

    for i in range(M):
        if v[N*M + i] == 2:
            archer.append(i)

    while True:
        kills = []
        for a in archer:
            visited = [0] * N * M
            zombie = []
            queue = [(N,a,0)]
            zombie_cnt = -1
            while queue:
                x, y, cnt = queue.pop(0)
                if cnt == D or (zombie_cnt !=-1 and cnt > zombie_cnt) : break
                for q in range(4):
                    nx, ny = x + dx[q], y + dy[q]
                    if 0 > nx or N <= nx or 0 > ny or M <= ny: continue
                    if visited[nx*M + ny]: continue
                    if v[nx*M + ny] == 1:
                        zombie.append((nx,ny))
                        queue.append((nx,ny,cnt+1))
                        zombie_cnt = cnt
                    elif v[nx*M + ny] == 0:
                        queue.append((nx,ny,cnt+1))
                    visited[nx*M + ny] = 1
            if zombie: kills.append(sorted(zombie, key=lambda x: x[1])[0])

        for kill in kills:
            x, y = kill
            if v[x*M+y] == 1:
                result += 1
                nowZombie -= 1
                v[x*M+y] = 0

        for i in range(M):
            if v[(N-1)*M + i] == 1:
                v[(N-1)*M + i] = 0
                nowZombie -= 1
        if nowZombie == 0: break

        for i in range(N-2, -1, -1):
            for j in range(M):
                if v[i*M+j] == 1:
                    v[i*M+j] = 0
                    v[(i+1)*M + j] = 1
        if nowZombie == 0: break
    maxV = max(maxV, result)

maxV = 0
put_archer(0,-1)
print(maxV)
