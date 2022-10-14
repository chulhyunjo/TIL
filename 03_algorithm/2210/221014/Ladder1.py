for _ in range(10):
    tc = int(input())
    graph = [list(map(int,input().split())) for _ in range(100)]
    startY = 0
    for i in range(100):
        if graph[99][i] == 2:
            startY = i
    x = 99
    while x>0:
        if startY - 1 >= 0 and graph[x][startY-1] == 1:
            while startY - 1 >= 0 and graph[x][startY-1] == 1:
                startY -= 1
        elif startY + 1 < 100 and graph[x][startY+1] == 1:
            while startY + 1 < 100 and graph[x][startY+1] == 1:
                startY += 1
        x -= 1
    print(f'#{tc} {startY}')