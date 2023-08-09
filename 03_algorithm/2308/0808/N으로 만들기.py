N = input()
n = len(N)
nums = list(N)
used = [False] * n


def dfs(num, d):
    global answer
    if d == n:
        if num == N:
            answer += 1
    else:
        for i in range(n):
            if not used[i]:
                used[i] = True
                dfs(num + nums[i], d+1)
                dfs(nums[i]+num, d+1)
                used[i] = False

answer = 0
for i in range(n):
    used[i] = True
    dfs(nums[i], 1)
    used[i] = False

print(answer)