for tc in range(1,11):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    graph_spin = list(map(list,zip(*graph[::-1])))
    # 1: N극, 2: S극
    for i in range(n):
        for j in range(n):
            if graph_spin[i][j] == 1:
                graph_spin[i][j] = 0
            if graph_spin[i][j] == 2:
                break
        for k in range(99,-1,-1):
            if graph_spin[i][k] == 1:
                break
            if graph_spin[i][k] == 2:
                graph_spin[i][k] = 0

    result = 0
    for i in range(n):
        now = 1
        for j in range(n):
            if now == 1 and graph_spin[i][j] == 2:
                now = 2
                result += 1
            if now == 2 and graph_spin[i][j] == 1:
                now = 1
    print(f'#{tc} {result}')