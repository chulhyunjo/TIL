n = int(input())
arr = list(map(int,input().split()))

checkArr = sorted(list(set(arr)))
result = dict()
for i in range(len(checkArr)):
    result[checkArr[i]] = i

for j in arr:
    print(f'{result[j]}', end = ' ')