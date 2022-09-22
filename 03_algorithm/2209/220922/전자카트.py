def combination(pre,i,o):
    global minV
    if i == n:
        battery = o + graph[pre-1][0]
        if battery < minV: minV = battery
    elif o > minV:
        return
    else:
        for j in range(2,n+1):
            if not visited[j]:
                visited[j] = 1
                combination(j,i+1, o+graph[pre-1][j-1])
                visited[j] = 0


for tc in range(1, int(input())+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    visited = [0] * (n+1)
    minV = int(1e9)
    combination(1,1,0)
    print(f'#{tc} {minV}')