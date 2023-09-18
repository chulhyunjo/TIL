N = int(input())
M = int(input())
position = list(map(int,input().split()))

s = position[0]
e = N
answer = 0

while s <= e:
    mid = (s+e) // 2

    pre = 0
    flag = 0
    for i in range(M):
        left = position[i] - mid if position[i] - mid > 0 else 0
        right = position[i] + mid if position[i] + mid < N else N
        if right == N:
            flag = 1
            break
        if left <= pre:
            pre = right
        else:
            break
    if flag:
        answer = mid
        e = mid - 1
    else:
        s = mid + 1

print(answer)