for tc in range(1,int(input())+1):
    n, m = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    t = 0
    while t < m:
        t += 1
        for i in range(n):
            for j in range(n):
                if m % t == 0:
                    graph[i][j] = (graph[i][j]+1)%2
                else:
                    if (i+j+2)%t == 0:
                        graph[i][j] = (graph[i][j]+1)%2
    result = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                result += 1
    print(f'#{tc} {result}')