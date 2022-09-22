for tc in range(1, int(input())+1):
    n = int(input())
    c = [list(map(int,input().split())) for _ in range(n)]
    c.sort(key=lambda x: (x[1],x[0]))
    r = 0
    e = 0
    for i in range(n):
        if c[i][0] >= e:
            e = c[i][1]
            r += 1
    print(f'#{tc} {r}')