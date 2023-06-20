number = input()


def findOdd(nums):
    cnt = 0
    for i in nums:
        for j in i:
            if int(j) % 2 == 1:
                cnt += 1
    return cnt


def dfs(d, r, nums, number, c):
    global minA, maxA
    if d == 3:
        cnt = findOdd(nums)
        sum1 = 0
        for i in nums:
            sum1 += int(i)
        dfs(0, 0, [], str(sum1), c + cnt)
    else:
        if len(number) == 1:
            cnt = findOdd([number])
            minA = min(c + cnt, minA)
            maxA = max(c + cnt, maxA)
            return
        elif len(number) == 2:
            dfs(3, 0, [number[0], number[1]], number, c)
        if len(number) >= 3:
            if d == 2:
                dfs(d+1, 0, nums + [number[r: len(number)]], number, c)
            else:
                for i in range(r, len(number)-2+d):
                    dfs(d+1, i + 1, nums + [number[r : i+1]], number, c)


minA = 10**6
maxA = 0
dfs(0, 0, [], number, 0)
print(minA, maxA)