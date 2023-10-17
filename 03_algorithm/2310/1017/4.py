def solution(n):
    if n < 10:
        return n

    answer = 0
    i = 0
    # 1자리:9개, 2자리:90개, 3자리:900개...
    while answer + 9 * (10 ** i) * (i + 1) < n:
        answer += 9 * (10 ** i) * (i + 1)
        i += 1

    # 자리수
    i += 1
    # n자리수 (10**(n-1))부터 몇번째
    nxt = n - answer
    print(nxt)
    if nxt // i == 0 or nxt // i == 1:  # 여기서 틀림
        number = (10 ** (i - 1)) + (nxt // i)
    else:
        number = (10 ** (i - 1)) + (nxt // i - 1)

    if nxt % i == 0:
        need = 1
    else:
        need = i - nxt % i + 1
    print(number, need)
    return number % (10 ** need) // (10 ** (need - 1))
