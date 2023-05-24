N, M, K = map(int,input().split())


pow_num = (N+M)
if pow(2,pow_num) < K:
    print(-1)
else:
    answer = [''] * pow_num
    turn = [0] * pow_num

    idx = 0
    while pow_num:
        pow_num -= 1
        turn[idx] = pow(2, pow_num)
        idx += 1

    idx = 0
    while N and M:
        if turn[idx+1] <= K:
            answer[idx] = 'z'
            M -= 1
            K -= turn[idx+1]
            idx += 1
        else:
            if N:
                answer[idx] = 'a'
                N -= 1
            else:
                answer[idx] = 'z'
                M -= 1
            idx += 1
    while N:
        answer[idx] = 'a'
        N -= 1
        idx += 1
    while M:
        answer[idx] = 'z'
        M -= 1
        idx += 1
    print(*answer,sep='')