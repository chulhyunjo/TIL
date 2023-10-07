N = int(input())
money = list(map(int,input().split()))
M = int(input())

s = 1
e = max(money)
answer = 0
while s <= e:
    mid = (s+e)//2

    cnt = 0
    for i in range(N):
        if money[i] <= mid:
            cnt += money[i]
        else:
            cnt += mid

        if cnt > M:
            break

    if cnt > M:
        e = mid - 1
    else:
        s = mid + 1
        answer = mid

print(answer)
