dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


c, r = map(int,input().split())
arr = [[0]*r for _ in range(c)]
i = 1
x = y = m = 0
k = int(input())
result = 0
while i <= r * c:
    arr[x][y] = i
    if i == k:
        result = [x,y]
        break
    nx = x + dx[m]
    ny = y + dy[m]
    if 0 <= nx < c and 0 <= ny < r and arr[nx][ny] == 0:
        x, y = nx, ny
    else:
        m = (m+1) % 4
        x = x + dx[m]
        y = y + dy[m]
    i += 1
if result:
    print(result[0]+1, result[1]+1)
else:
    print(0)