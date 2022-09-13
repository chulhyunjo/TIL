bingo = [list(map(int,input().split())) for _ in range(5)]
bingo2 = list(map(list, zip(*bingo)))
say = []
for _ in range(5):
    say += list(map(int,input().split()))
cnt = 0

while True:
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == say[cnt]:
                bingo[i][j] = 0
                bingo2[j][i] = 0
    cnt += 1
    bingo_dia = []
    bingo_dia2 = []
    for i in range(5):
        bingo_dia += [bingo[i][i]]
        bingo_dia2 += [bingo[i][5-i-1]]

    result = 0
    for q in range(5):
        if sum(bingo[q]) == 0:
            result += 1
        if sum(bingo2[q]) == 0:
            result += 1
    if sum(bingo_dia)== 0:
        result += 1
    if sum(bingo_dia2) == 0:
        result += 1
    if result >= 3:
        break

print(cnt)