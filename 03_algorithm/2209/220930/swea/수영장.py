def search(d, money):
    global minV
    if d >= 12:
        if money < minV:
            minV = money

    elif money >= membership[3]:
        return
    else:
        if d < 12:
            if plan[d] > 0:
                search(d + 1, money + min(membership[0] * plan[d],membership[1]))
                search(d + 3, money + membership[2])
            else:
                search(d + 1, money)


for tc in range(1, int(input()) + 1):
    membership = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    minV = membership[3]
    search(0, 0)
    print(f'#{tc} {minV}')