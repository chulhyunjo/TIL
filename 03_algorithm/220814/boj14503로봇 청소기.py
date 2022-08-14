from pprint import pprint
n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r, c, d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
if arr[r][c] == 0:
    arr[r][c] = 2
    cnt += 1
while True:
    if arr[r+dx[d]][c+dy[d]] == 1:
        r = r - dx[d]
        c = c - dy[d]
    for i in range(1,5):
        nr = r + dx[(d-i+4) % 4]
        nc = c + dy[(d-i+4) % 4]
        if  0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1:
            r = r - dx[(d-i+4) % 4]
            c = c - dy[(d-i+4) % 4]
        elif 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
            arr[nr][nc] = 2
            cnt += 1
            r, c = nr, nc
            d = (d-i+4) % 4
            break
    else:
        r = r - dx[d]
        c = c - dy[d]
        if arr[r + dx[d]][c + dy[d]] == 1:
            r = r - dx[d]
            c = c - dy[d]
        for j in range(1,5):
            nr = r + dx[(d-j+4) % 4]
            nc = c + dy[(d-j+4) % 4]
            if  0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1:
                r = r - dx[(d - i + 4) % 4]
                c = c - dy[(d - i + 4) % 4]
            elif 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
                arr[nr][nc] = 2
                cnt += 1
                r, c = nr, nc
                d = (d - i + 4) % 4
                break
        else:
            break
print(cnt)
pprint(arr)