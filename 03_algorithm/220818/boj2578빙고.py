arr = [list(map(int,input().split())) for _ in range(5)]
say = []
row_arr = list(map(list,zip(*arr)))
for _ in range(5):
    say += list(map(int,input().split()))
m = 0

while True:
    for i in range(5):
        for j in range(5):
            if arr[i][j] == say[m]:
                arr[i][j] = 0
                row_arr[j][i] = 0
    m += 1
    arrow1 = []
    arrow2 = []
    for i in range(5):
        arrow1 += [arr[i][i]]
        arrow2 += [arr[i][4-i]]
    bingo =0
    for q in range(5):
        if sum(arr[q]) == 0:
            bingo += 1
        if sum(row_arr[q]) == 0:
            bingo += 1
    if not sum(arrow1):
        bingo += 1
    if not sum(arrow2):
        bingo += 1
    if bingo >= 3 :
        break

print(m)