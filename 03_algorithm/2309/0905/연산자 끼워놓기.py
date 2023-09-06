def dfs(d, now):
    global max_num, min_num
    if d == N:
        max_num = max(max_num, now)
        min_num = min(min_num, now)
        return
    if cnt[0]:
        cnt[0] -= 1
        dfs(d+1, now + numbers[d])
        cnt[0] += 1
    if cnt[1]:
        cnt[1] -= 1
        dfs(d+1, now - numbers[d])
        cnt[1] += 1
    if cnt[2]:
        cnt[2] -= 1
        dfs(d+1, now * numbers[d])
        cnt[2] += 1
    if cnt[3]:
        cnt[3] -= 1
        if now < 0:
            dfs(d+1, -(-now // numbers[d]))
        else:
            dfs(d+1, now // numbers[d])
        cnt[3] += 1

N = int(input())
numbers = list(map(int,input().split()))
cnt = list(map(int,input().split()))

max_num = -int(1e9)
min_num = int(1e9)

dfs(1, numbers[0])
print(max_num, min_num, sep='\n')