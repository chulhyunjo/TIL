n = int(input())
arr = list(map(int,input().split()))

cnt = 1
cnt1 = 1
result = 0
if n == 1:
    result = 1
else:
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            cnt += 1
            cnt1 = 1
        elif arr[i] < arr[i-1]:
            cnt1 += 1
            cnt = 1
        else:
            cnt += 1
            cnt1 +=1

        result = max(result, cnt, cnt1)

print(result)