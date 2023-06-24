N, K = map(int,input().split())

s = 0
e = N
answer = 'NO'
while s <= e:
    mid = (s+e) // 2

    nums = (mid+1) * (N-mid+1)
    if nums == K:
        answer = 'YES'
        break

    elif nums > K:
        e = mid - 1

    else:
        s = mid + 1

print(answer)