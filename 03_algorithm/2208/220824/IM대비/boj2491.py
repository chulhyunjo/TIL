n = int(input())
arr = list(map(int,input().split()))

increase = 1
decrease = 1
result = 1
for i in range(1,n):
    if arr[i] > arr[i-1]:
        increase += 1
        decrease = 1

    elif arr[i] < arr[i-1]:
        increase = 1
        decrease += 1

    else:
        increase += 1
        decrease += 1

    result = max(increase,decrease,result)

print(result)