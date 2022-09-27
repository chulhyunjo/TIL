def put_queen(now_y):
    global ans
    if now_y == N:
        ans += 1
        return

    for i in range(N):
        if used[i] != -1:
            continue
        if now_y == 0:
            used[i] = now_y
            put_queen(now_y + 1)
            used[i] = -1
        else:
            flag = 0
            for j in range(N):
                if used[j] != -1:
                    if abs(j - i) == abs(used[j] - now_y):
                        flag = 1
                        break
            if flag == 1:
                continue
            used[i] = now_y
            put_queen(now_y + 1)
            used[i] = -1

N = int(input())
used = [-1] * N
ans = 0
put_queen(0)
print(ans)