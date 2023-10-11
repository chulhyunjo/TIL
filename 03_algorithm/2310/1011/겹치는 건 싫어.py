N, K = map(int,input().split())
numbers = list(map(int,input().split()))

s, e = 0, 0
cnt = [0] * (max(numbers)+1)
cnt[numbers[s]] += 1

answer = 0
while e < N-1:
    e += 1
    cnt[numbers[e]] += 1
    while cnt[numbers[e]] > K:
        cnt[numbers[s]] -= 1
        s += 1
    answer = max(e - s + 1, answer)

print(answer)