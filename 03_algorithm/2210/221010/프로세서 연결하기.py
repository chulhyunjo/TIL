def findDir(x,y, g):
    posDir = []
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x+dx, y+dy
        flag = 1
        while 0 <= nx < n and 0 <= ny < n:
            if g[nx][ny] == 1:
                flag = 0
                break
            nx, ny = nx+dx, ny+dy
        if flag: posDir.append((dx,dy))
    return posDir

def play(d,result, graph, core, rs):
    global minV, maxCore
    if d == len(position):
        if core > maxCore:
            maxCore = core
            minV = result
        elif core == maxCore:
            minV = min(minV, result)
        return
    if core + rs < maxCore: return
    x, y = position[d]
    direction = findDir(x,y,graph)
    if direction:
        for dx, dy in direction:
            cnt = result
            new_graph = []
            for i in range(n):
                new_graph.append(graph[i][:])
            nx, ny = x+dx, y+dy
            while 0 <= nx < n and 0 <= ny < n:
                new_graph[nx][ny] = 1
                cnt += 1
                nx, ny = nx+dx, ny+dy
            play(d+1, cnt, new_graph, core+1, rs-1)
    else:
        play(d+1, result, graph, core, rs-1)


for tc in range(1, int(input())+1):
    n = int(input())
    graph = []
    position = []
    for i in range(n):
        line = list(map(int,input().split()))
        graph.append(line)
        if 0 < i < n-1:
            for j in range(n):
                if 0 < j < n-1 and line[j] == 1:
                    position.append((i,j))
    minV = 12*12
    maxCore = 0
    play(0,0,graph,0, len(position))

    print(f'#{tc} {minV}')