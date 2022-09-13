x,y = map(int,input().split()) # x: 가로, y: 세로
n = int(input()) # 자른 횟수
cols = [0]
rows = [0]
for _ in range(n):
    dic, idx = map(int,input().split())
    if dic:
        rows.append(idx)
    else:
        cols.append(idx)
cols = sorted(cols) + [y]
rows = sorted(rows) + [x]
area = 0
for i in range(1,len(cols)):
    for j in range(1, len(rows)):
        now_area = (cols[i] - cols[i-1]) * (rows[j] - rows[j-1])
        area = max(now_area, area)

print(area)