for t in range(1, int(input())+1):
    n, m = map(int,input().split())
    graph = [list(input()) for _ in range(n)]
    result = 'YES'
    for i in range(n):
        for j in range(m):
            if i < n-1 and j < m - 1 and graph[i][j] == '#':
                if graph[i+1][j] == graph[i][j+1] == graph[i+1][j+1] == '#':
                    graph[i][j] = graph[i + 1][j] = graph[i][j + 1] = graph[i + 1][j + 1] = '.'
                else:
                    result = 'NO'
                    break
            if i == n-1 or j == m-1:
                if graph[i][j] == '#':
                    result = 'NO'
                    break
        if result == 'NO':
            break
    print(f'#{t} {result}')