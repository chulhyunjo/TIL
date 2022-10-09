def check(x,y):
    a1 = a2 = a3 = a4 = 0
    for i in range(n):
        for j in range(n):
            if i < x and j < y:
                a1 += graph[i][j]
            elif x <= i < n and j < y:
                a2 += graph[i][j]
            elif i < x and y <= j < n:
                a3 += graph[i][j]
            else:
                a4 += graph[i][j]
    return max(a1,a2,a3,a4) - min(a1,a2,a3,a4)


for tc in range(1, int(input())+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    result = 40000
    for i in range(1, n):
        for j in range(1, n):
            result = min(check(i,j), result)
    print(f'#{tc} {result}')