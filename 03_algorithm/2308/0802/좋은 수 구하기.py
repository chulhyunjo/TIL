N = int(input())
nums = list(map(int,input().split()))
nums.sort()
K = 0
answer = 0
while K < N:
    s = 0
    e = N-1
    while s < e:
        sums = nums[s] + nums[e]
        if sums == nums[K]:
            if s != K and e != K:
                answer += 1
                break
            elif s == K:
                s += 1
            elif e == K:
                e -= 1
        elif sums < nums[K]:
            s += 1
        else:
            e -= 1
    K += 1
print(answer)