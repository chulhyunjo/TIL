N = int(input())
M = int(input())
nums = list(map(int,input().split()))
nums.sort()

s = 0
e = N-1

answer = 0
while s < e:
    sums = nums[s] + nums[e]
    if sums == M:
        answer += 1
        s += 1
        e -= 1

    elif sums > M:
        e -= 1

    else:
        s += 1

print(answer)