def findSquare(x,y):
    size = []
    for d in range(5, 0, -1):
        for i in range(x, x+d):
            for j in range(y, y+d):
                flag = 0
                if 0<=i<10 and 0<=j<10:
                    if graph[i][j] != 1:
                        flag = 1
                        break
                else:
                    flag = 1
                    break
            if flag: break
        else: size.append(d)
    return size


def putPapper(x, y, size, number):
    for i in range(x,x+size):
        for j in range(y, y+size):
            graph[i][j] = number


def backtracking(d):
    global result, total
    if not total:
        result = min(result, d)
        return
    if d > result: return
    for i in range(10):
        for j in range(10):
            if graph[i][j] == 1:
                sizes = findSquare(i,j)
                for size in sizes:
                    if paper[size]:
                        paper[size] -= 1
                        putPapper(i,j,size, size+1)
                        total -= size * size
                        backtracking(d+1)
                        total += size * size
                        putPapper(i, j, size, 1)
                        paper[size] += 1
                else: return


graph = [list(map(int,input().split())) for _ in range(10)]
paper = [0,5,5,5,5,5]

total = 0
for i in range(10):
    for j in range(10):
        if graph[i][j] == 1:
            total += 1
if total == 0:
    result = 0
else:
    used = [0] * 6
    result = 26
    backtracking(0)
if result != 26:
    print(result)
else:
    print(-1)