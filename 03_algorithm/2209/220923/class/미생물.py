dx = [1,-1]
for tc in range(1, int(input())+1):
    N, M, K = map(int,input().split())
    info = [list(map(int,input().split())) for _ in range(K)]
    T = 0
    while T < M:
        location = dict()
        for i in range(len(info)):
            x, y, num, d = info[i][0],info[i][1],info[i][2],info[i][3]
            if d >=3:
                y += dx[d % 2]
            else:
                x += dx[d % 2]
            if x == 0 or y == 0 or x == N-1 or y == N-1:
                num //= 2
                if d in [1,3]: d+=1
                else : d -= 1
            location[(x,y)] = location.get((x,y),[]) + [[x,y,num,d]]

        info = []
        for v in location.values():
            if len(v) == 1:
                if v[0][2] == 0: continue
                info.append(v[0])
                continue
            else:
                nums = maxV = direction = 0
                x,y = v[0][0], v[0][1]
                for i in v:
                    nums += i[2]
                    if i[2] > maxV:
                        maxV = i[2]
                        direction = i[3]
                info.append([x,y,nums,direction])
        T += 1

    result = 0
    for i in info:
        result += i[2]
    print(f'#{tc} {result}')
