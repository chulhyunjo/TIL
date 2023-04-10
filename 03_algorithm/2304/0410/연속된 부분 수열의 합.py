def solution(sequence, k):
    answer = [0, 0]
    end = len(sequence)
    s = 0
    e = 1
    sequenceLen = 1000000

    sum1 = sequence[s] + sequence[e]

    while e < end:
        if sum1 == k:
            if sequenceLen > (e - s + 1):
                answer[0] = s
                answer[1] = e
                sequenceLen = e - s + 1

        if sum1 >= k:
            sum1 -= sequence[s]
            s += 1
            if s == e:
                if e == end: break
                e += 1
                sum1 += sequence[e]

        else:
            if e == end: break
            e += 1
            sum1 += sequence[e]

    return answer

solution(	[1, 1, 1, 2, 3, 4, 5],7)