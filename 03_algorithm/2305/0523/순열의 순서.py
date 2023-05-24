N = int(input())
cmd, *nums = map(int,input().split())

p = 1
cnt = [0] * N
for i in range(1, N+1):
    p *= i
    cnt[N-i] = p

used = [False] * N
if cmd == 1:
    answer = [0] * N
    num = nums[0]
    idx = 0
    while idx < N-1:
        if cnt[idx+1] > num:
            for i in range(N):
                if not used[i]:
                    answer[idx] = i+1
                    used[i] = True
                    idx += 1
                    break

        else:
            count = 1
            while count * cnt[idx+1] < num:
                count += 1
            n = 0
            for i in range(N):
                if not used[i]:
                    n += 1

                if n == count:
                    answer[idx] = i+1
                    num = num - ((count-1)*cnt[idx+1])
                    used[i] = True
                    break
            idx += 1
    for i in range(N):
        if not used[i]:
            answer[-1] = i+1
    print(*answer)

else:
    idx = 0
    K = 1
    while idx < N:
        count = 0
        for i in range(1,N+1):
            if not used[i-1]:
                if i == nums[idx]:
                    used[i-1] = True
                    break
                else:
                    count += 1
        if count:
            K = K + count * cnt[idx+1]
        idx += 1
    print(K)