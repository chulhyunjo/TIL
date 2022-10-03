def dijkstra(N, S, d):
    for j in range(len(adjL[S])):
        d[adjL[S][j][0]] = adjL[S][j][1]

    U = [S] # 출발지만
    for _ in range(N-1):    # N개의 정점 중 출발을 제외한 정점 선택
        w = 0
        for i in range(1, N+1):
            if (i not in U) and d[i] < d[w]: # 남은 노드 중 비용이 최소인 w
                w = i
        U.append(w)
        for v in range(1, N+1):             # 정점 i가
            if 0 < adjL[w][v] < 100000:      # w에 인접이면
                d[v] = min(d[v], d[w] + adjL[w][v])



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())

    adjL = [[] for _ in range(n+1)]

    for i in range(n-1):
        for j in range(i+1, n):
            L = (X[i] - X[j])**2 + (Y[i] - Y[j]) ** 2
            adjL[i+1].append((j+1,E*L))
            adjL[j+1].append((i+1,E*L))
    print(adjL)
    dist = [0] * (n+1)
    dijkstra(0,1,dist)
    print(dist)