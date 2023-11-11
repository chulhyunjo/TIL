N = int(input())
nums = list(map(int,input().split()))
answer = 0
for i in range(N):
    num = nums[i]
    leftnums = nums[:i]
    rightnums = nums[i+1: N]
    sum1 = 0
    if leftnums:
        sum1 += sum(leftnums)
    if rightnums:
        sum1 += sum(rightnums)

    if num == sum1 / (N-1):
        print(nums[i])
        answer += 1

print(answer)

