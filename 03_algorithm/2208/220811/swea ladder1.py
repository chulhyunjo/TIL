dx = [0, 0, -1]
dy = [1, -1, 0]

for t in range(10):
    tc = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    row = 99 # 맨 아래에서부터 시작
    col = 0 # 2의 값을 찾을 변수 선언
    for i in range(100):
        if arr[row][i] == 2:
            col = i

    while row > 0:
        for move in range(3): # 좌, 우 사다리가 있는지 먼저 확인하고 위로 올라가기
            nx = row + dx[move]
            ny = col + dy[move]
            # 범위 안에 있고 사다리가 있거나 방문하지 않았으면 이동.
            if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] == 1:
                arr[nx][ny] = -1
                row, col = nx, ny
                break

    print(f"#{tc} {col}")
