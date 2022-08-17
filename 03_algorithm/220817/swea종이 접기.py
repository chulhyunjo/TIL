arr = [0] * 31
arr[1] = 1
arr[2] = 3
for i in range(3,31):
    if i % 2:
        arr[i] = arr[i-1] * 2 -1
    else:
        arr[i] = arr[i-1] * 2 + 1

for tc in range(1, int(input())+1):
    n = int(input())
    print(f'#{tc} {arr[n//10]}')