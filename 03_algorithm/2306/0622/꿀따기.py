N = int(input())
nums = list(map(int,input().split()))

sums = [0] * N
sums[0] = nums[0]
for i in range(1,N):
    sums[i] += nums[i] + sums[i-1]

answer = 0
for i in range(1, N-1):
    answer = max(answer, sums[-1] - nums[-1] + sums[i] - 2* nums[i])
    answer = max(answer, sums[-1] - nums[-1] + nums[i] - nums[0])
    answer = max(answer, sums[-1] - nums[0] + sums[-1] - sums[i] - nums[i])
    
print(answer)