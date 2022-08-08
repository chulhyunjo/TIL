n = int(input())

cnts = [0] * 10

while n:
    cnts[n % 10] += 1
    n //= 10

cnt = 0
result = 0
i = 0
while i <= 9:
    if cnts[i] >= 3:
        result += 1
        cnts[i] -= 3

    if cnts[i] != 0:
        cnt += 1
        cnts[i] -= 1
    else:
        cnt = 0

    if cnt == 3:
        result += 1
        i -= 3
    else:
        i += 1

print(result)