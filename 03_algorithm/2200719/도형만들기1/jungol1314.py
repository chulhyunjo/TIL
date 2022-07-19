n = int(input())
num = 65
array = [[0] * n for _ in range(n)]

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            array[j][i] = chr(num)
            num += 1
            if num > 90:
                num = 65
    else:
        for j in range(n-1,-1,-1):
            array[j][i] = chr(num)
            num += 1
            if num > 90:
                num = 65
for k in array:
    print(*k)