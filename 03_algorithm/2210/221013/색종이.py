graph = [[0]*1001 for _ in range(1001)]
n = int(input())
result = [0]*(n+1)
for i in range(1,n+1):
    x1, y1, dx, dy = map(int,input().split())
    for x in range(x1,x1+dx):
        for y in range(y1,y1+dy):
            if graph[x][y] == 0:
                graph[x][y] = i
                result[i] += 1
            elif graph[x][y] != 0:
                result[graph[x][y]] -= 1
                graph[x][y] = i
                result[i] += 1

for r in result[1:]:
    print(r)