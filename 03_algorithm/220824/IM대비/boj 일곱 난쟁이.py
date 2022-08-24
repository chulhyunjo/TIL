seven = []
for _ in range(9):
    seven.append(int(input()))


for i in range(1,1 << 9):
    cnt = 0
    result = []
    for j in range(9):
        if i & (1 << j):
            result.append(seven[j])
            cnt += 1

    if cnt == 7 and sum(result) == 100:
        for j in sorted(result):
            print(j)
        break
