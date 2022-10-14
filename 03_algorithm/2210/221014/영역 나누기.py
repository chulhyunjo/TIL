for tc in range(1, int(input())+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    minV = 100 * 20 * 20
    for i in range(1,n):
        for j in range(1,n):
            q=w=e=r=0
            for a in range(i):
                for b in range(j):
                    q += graph[a][b]
            for a in range(i,n):
                for b in range(j):
                    w += graph[a][b]
            for a in range(i):
                for b in range(j,n):
                    e += graph[a][b]
            for a in range(i,n):
                for b in range(j,n):
                    r += graph[a][b]
            minV = min(minV, max(q,w,e,r) - min(q,w,e,r))
    print(f'#{tc} {minV}')