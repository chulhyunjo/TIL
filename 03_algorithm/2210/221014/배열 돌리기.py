n,m,r = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
t = 0
new_graph = [a[:] for a in graph]
next_graph = [a[:] for a in new_graph]
startX , startY = 0,0
endX, endY = n-1,n-1
while startX < endX and startY < endY:
    for _ in range(r):
        for i in range(startY+1, endY+1):
            next_graph[endX][i] = new_graph[endX][i-1]
        for i in range(startX+1,endX+1):
            next_graph[i][startY] = new_graph[i-1][startY]
        for i in range(endY-1,startY-1,-1):
            next_graph[startX][i] = new_graph[startX][i+1]
        for i in range(endX-1,startX-1,-1):
            next_graph[i][endY] = new_graph[i+1][endY]
        new_graph = [a[:] for a in next_graph]
    startX += 1
    startY += 1
    endX -= 1
    endY -= 1
for line in new_graph:
    print(*line)
