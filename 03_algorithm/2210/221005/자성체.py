for tc in range(1, 11):
    n = input()
    graph = [list(map(int,input().split())) for _ in range(100)]
    # 1: N , 2: S
    result = 0
    for i in range(100):
        N = 2
        for j in range(100):
            if graph[j][i] == 1:
                N = 1
            elif N == 1 and graph[j][i] == 2:
                result += 1
                N = 2
    print(f'#{tc} {result}')