def solution(diffs, times, limit):
    N = len(diffs)
    s = 0
    e = max(diffs)

    answer = 0
    while s<=e:
        mid = (s+e) // 2
        time = 0

        for i in range(N):
            if diffs[i] <= mid:
                time += times[i]
            else:
                time += (diffs[i] - mid) * (times[i] + times[i-1]) + times[i]

            if time > limit:
                s = mid + 1
                break
        else:
            e = mid - 1
            answer = mid

    return answer