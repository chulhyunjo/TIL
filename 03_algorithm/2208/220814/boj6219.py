def eratos(x,y):
    table = [True] * (y+1)
    table[0] = False
    table[1] = False

    for i in range(2, int(y ** 0.5) + 1):
        if table[i] == True:
            for j in range(i + i, y + 1, i):
                table[j] = False
    return [k for k in range(x, y+1) if table[k] == True]


a, b, d = map(int, input().split())
d = str(d)
cnt = 0
arr = eratos(a,b)
for i in arr:
    if d in str(i):
        cnt += 1
print(cnt)