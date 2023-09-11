N, K = map(int,input().split())
scores = list(map(int,input().split()))

s = 0
e = 20 * N
answer = 0

if K == 1:
    print(sum(scores))
else:
    while s <= e:
        mid = (s+e) // 2

        cnt = 0
        score = 0
        for i in range(N):
            score += scores[i]
            if score >= mid:
                cnt += 1
                score = 0
        # if score:
        #     cnt += 1

        if cnt > K-1:
            answer = mid
            s = mid + 1
        else:
            e = mid - 1
    print(answer)