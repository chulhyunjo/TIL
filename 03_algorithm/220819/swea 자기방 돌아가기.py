for tc in range(1, int(input())+1):
    n = int(input())
    rooms = []

    for _ in range(n):
        a, b = map(int,input().split())
        if a > b:
            a, b = b, a
        rooms.append([(a+1)//2,(b+1)//2])
    now_range = [0] * 201
    while rooms:
        x, y = rooms.pop()
        for i in range(x,y+1):
            now_range[i] += 1

    print(f'#{tc} {max(now_range)}')