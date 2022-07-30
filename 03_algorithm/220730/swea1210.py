dx = [0, 0, -1]
dy = [1, -1, 0]

for t in range(10):
    tc = int(input())

    ladders = [list(map(int, input().split())) for _ in range(100)]

    x = 99
    y = ladders[99].index(2)
    visited = set()
    visited.add((x,y))

    while x > 0:
        for move in range(3):
            nx = x + dx[move]
            ny = y + dy[move]

            if nx < 0 or ny < 0 or ny > 99:
                continue

            if (nx, ny) in visited:
                continue

            if ladders[nx][ny] == 1:
                visited.add((nx, ny))
                x, y = nx, ny
                break

    print(f"#{tc} {y}")