for tc in range(1,int(input())+1):
    N = int(input())
    graph =[]
    for x in range(N):
        line = list(map(int,input().split()))
        for y in range(N):
            graph.append([x,y,line[y]])
    graph.sort(key=lambda x: x[2])
    dp = [1] * (N**2)
    for i in range(N**2-1):
        if abs(graph[i][0] - graph[i+1][0]) + abs(graph[i][1] - graph[i+1][1]) == 1:
            dp[i+1] = dp[i]+1

    print(dp)
    maxV = max(dp)
    print(f'#{tc} {dp.index(maxV)+1} {maxV}')
