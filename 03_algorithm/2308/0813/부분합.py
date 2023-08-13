N, S = map(int,input().split())
nums = list(map(int,input().split()))
if sum(nums) < S:
    print(0)
else:
    min_length = N
    s = 0
    e = 1
    sum1 = nums[0]
    while e <= N and s <= N:

        if sum1 >= S:
            min_length = min(min_length, e-s)
            sum1 -= nums[s]
            s += 1
        else:
            if e == N:
                break
            sum1 += nums[e]
            e += 1

    print(min_length)