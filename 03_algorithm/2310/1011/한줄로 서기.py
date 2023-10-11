N = int(input())
nums = [0] + list(map(int,input().split()))

line = [0] * (N+1)

for i in range(1,N+1):
    num = nums[i]
    cnt = 0
    for j in range(1, N+1):
        if cnt == num and not line[j]:
            line[j] = i
            break
        if not line[j]:
            cnt += 1

print(*line[1:])