n = int(input())
arr = [0] * 30001

for i in range(1,n+1):
    # 현재의 수에서 1을 빼는 경우
    arr[i] = arr[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 5:
        arr[i] = min(arr[i],arr[i//5] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3:
        arr[i] = min(arr[i],arr[i//3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 2:
        arr[i] = min(arr[i],arr[i//2] + 1)

print(arr[n])