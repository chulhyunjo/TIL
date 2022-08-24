w, h = map(int,input().split())
n = int(input())
rows = [0]
cols = [0]
for _ in range(n):
    a, b = map(int,input().split())
    if a:
        rows.append(b)
    else:
        cols.append(b)

rows = sorted(rows) + [w]
cols = sorted(cols) + [h]
result = 0
for i in range(1,len(rows)):
    for j in range(1,len(cols)):
        area = (rows[i] - rows[i-1]) * (cols[j] - cols[j-1])
        result = max(result, area)

print(result)