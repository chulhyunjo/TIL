import sys
sys.setrecursionlimit(10**5)


def f(arr,i,j,s,h):
    if i == h:
        if j == s:
            return 1
    else:
        arr[i][j] = 0
        for di, dj in [[0,1],[0,-1],[1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<=h and 0<=nj<(n*2-1) and arr[ni][nj] == 1:
                if f(arr,ni,nj,s,h):
                    return 1
                break   # break 추가
    return 0


def repeat(arr):
    cnt = 0
    for t in range(n):
        arr_cp = []
        for i in range(h+2):
            arr_cp.append(arr[i][:])
        if f(arr_cp, 0, t * 2, t * 2, h+1):
            cnt += 1
        else:
            break
    if cnt == n:
        return 1
    else:
        return 0


def add(k):
    vis = [[0]*(n*2-1) for _ in range(h+2)]
    if k == 0:
        if repeat(arr):
            return 1
        else:
            return 0
    if k == 1:
        for p in range(1,h+1):
            for q in range(1,n*2-2,2):
                if arr[p][q] == 0:
                    check = 0
                    if n == 2:
                        arr[p][q] = 1
                        if repeat(arr):
                            return 1
                        else:
                            arr[p][q] = 0
                    else:
                        if q-2 >= 1 and q+2 < n*2-2:
                            if arr[p][q-2] ==0 and arr[p][q+2] ==0:
                                check = 1
                        elif q-2 >= 1:
                            if arr[p][q-2] ==0:
                                check = 1
                        elif q+2 < n*2-2:
                            if arr[p][q+2] ==0:
                                check = 1
                        if check:
                            arr[p][q] = 1
                            if repeat(arr):
                                return 1
                            else:
                                arr[p][q] = 0
    elif k == 2:
        for p in range(1,h+1):
            for q in range(1,n*2-2,2):
                if arr[p][q] == 0:
                    check1 = 0
                    if q-2 >= 1 and q+2 < n*2-2:
                        if arr[p][q-2] ==0 and arr[p][q+2] ==0:
                            check1 = 1
                    elif q-2 >= 1:
                        if arr[p][q-2] ==0:
                            check1 = 1
                    elif q+2 < n*2-2:
                        if arr[p][q+2] ==0:
                            check1 = 1
                    if check1:
                        vis[p][q] = 1
                        arr[p][q] = 1
                        for v in range(p,h+1):
                            for w in range(1,n*2-2,2):
                                if arr[v][w] == 0:
                                    check2 = 0
                                    if w-2>=1 and w+2 < n*2-2:
                                        if arr[v][w-2] == 0 and arr[v][w+2] == 0 and vis[v][w] == 0:
                                            check2 = 1
                                    elif w-2 >= 1:
                                        if arr[v][w-2] == 0 and vis[v][w] == 0:
                                            check2 = 1
                                    elif w + 2 < n * 2 - 2 and vis[v][w] == 0:
                                        if arr[v][w + 2] == 0:
                                            check2 = 1
                                    if check2:
                                        arr[v][w] = 1
                                        if repeat(arr):
                                            return 1
                                        else:
                                            arr[v][w] = 0
                        arr[p][q] = 0
    elif k == 3:
        for p in range(1,h+1):
            for q in range(1,n*2-2,2):
                if arr[p][q] == 0:
                    check1 = 0
                    if q - 2 >= 1 and q + 2 < n * 2 - 2:
                        if arr[p][q - 2] == 0 and arr[p][q + 2] == 0:
                            check1 = 1
                    elif q - 2 >= 1:
                        if arr[p][q - 2] == 0:
                            check1 = 1
                    elif q + 2 < n * 2 - 2:
                        if arr[p][q + 2] == 0:
                            check1 = 1
                    if check1:
                        vis[p][q] = 1
                        arr[p][q] = 1
                        for v in range(p, h + 1):
                            for w in range(1, n * 2 - 2, 2):
                                if arr[v][w] == 0:
                                    check2 = 0
                                    if w - 2 >= 1 and w + 2 < n * 2 - 2:
                                        if arr[v][w - 2] ==0 and arr[v][w + 2] ==0 and vis[v][w] == 0:
                                            check2 = 1
                                    elif w - 2 >= 1:
                                        if arr[v][w - 2] ==0 and vis[v][w] == 0:
                                            check2 = 1
                                    elif w + 2 < n * 2 - 2 and vis[v][w] == 0:
                                        if arr[v][w + 2] == 0:
                                            check2 = 1
                                    if check2:
                                        arr[v][w] = 1
                                        for x in range(v,h+1):
                                            for y in range(1,n*2-2,2):
                                                if arr[x][y] == 0:
                                                    check3=0
                                                    if y-2>=1 and y+2 < n*2-2:
                                                        if arr[x][y-2] ==0 and arr[x][y+2]==0 and vis[x][y] == 0:
                                                            check3 = 1
                                                    elif y-2 >=1:
                                                        if arr[x][y-2]==0 and vis[x][y] == 0:
                                                            check3 =1
                                                    elif y + 2 < n * 2 - 2 and vis[x][y] == 0:
                                                        if arr[x][y + 2] == 0:
                                                            check3 = 1
                                                    if check3:
                                                        arr[x][y] = 1
                                                        if repeat(arr):
                                                            return 1
                                                        else:
                                                            arr[x][y] = 0
                                        arr[v][w] = 0
                        arr[p][q] = 0

    return 0


n,m,h = map(int, sys.stdin.readline().split())

if m == 0:
    print(0)
else:
    arr = [[0]*(n*2-1) for _ in range(h+2)]
    for i in range(h+2):
        for j in range(0,n*2-1,2):
            arr[i][j] = 1

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        arr[a][b*2-1] = 1

    # 사다리가 홀수 개인 곳이 3개 초과면 X
    odd = 0
    line = [0] * (n-1)
    for i in range(h+2):
        for j in range(1,n*2-1,2):
            if arr[i][j] == 1:
                line[j//2] += 1
    for i in line:
        if i%2:
            odd += 1

    if odd > 3:
        print(-1)
        exit()

    if add(0):
        print(0)
    elif add(1):
        print(1)
    elif add(2):
        print(2)
    elif add(3):
        print(3)
    else:
        print(-1)