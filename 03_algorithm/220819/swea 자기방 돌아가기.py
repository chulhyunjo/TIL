for tc in range(1, int(input())+1):
    n = int(input())
    rooms = []

    for _ in range(n):
        rooms.append(list(map(int,input().split())))

    # while rooms:
    now_range = [0] * 401
    for room in rooms:
        x, y = room[0], room[1]
        if now_range[x:y+1].count(1):
            continue
        else:
            now_range[x:y+1] = [1] * (y-x)
    print(now_range)