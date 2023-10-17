def solution(s):
    N = len(s)
    # 0:유지, 1: 증가, 2: 감소
    flag = 1
    cnt = 0

    if s[0] < s[1]:
        flag = 1
    else:
        cnt += 1
        if s[0] == s[1]:
            flag = 0
        else:
            flag = 2

    for i in range(2, N):
        if s[i] > s[i-1]:
            if flag == 2:
                flag = 1
            else:
                if s[i] == s[i-1]:
                    flag = 0
                cnt += 1

        elif s[i] < s[i-1]:
            if flag == 1:
                flag = 2
            else:
                if s[i] == s[i-1]:
                    flag = 0
                cnt += 1

        else:
            flag = 0
            cnt += 1

    return cnt

