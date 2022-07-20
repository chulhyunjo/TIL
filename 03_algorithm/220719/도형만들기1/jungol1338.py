n = int(input())
array = [[0]*i for i in range(1,n+1)]

num = 65
for i in range(n):
    for j in range(i,n):
        array[j][i] = chr(num)
        num += 1
        if num > 90:
            num = 65

for i in range(n):
    for j in range(n-i-1,0, -1):
        print(' ', end = ' ')
    print(*array[i])