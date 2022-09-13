import sys
n = int(sys.stdin.readline())
array1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
array2 = list(map(int, sys.stdin.readline().split()))

result = dict()
for i in array1:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

for j in array2:
    if j in result:
        print(result[j], end = ' ')
    else:
        print(0, end= ' ')