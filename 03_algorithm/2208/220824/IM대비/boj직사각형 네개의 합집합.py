graph = [[0] * 101 for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1
area = 0
for i in graph:
    area += i.count(1)
print(area)