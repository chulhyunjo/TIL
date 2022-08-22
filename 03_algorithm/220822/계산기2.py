for tc in range(1, 11):
    n = int(input())
    sen = input()

    stack_num = []                          # 숫자를 담을 리스트
    i = 0                                   # 확인할 인덱스
    while i < n:
        if sen[i] == '+':                   # + 일경우 생략
            i += 1
            continue

        elif sen[i] == '*':                 # * 일 경우 다음 숫자와 전숫자를 곱해서 리스트에 담는다
            i += 1                          # * 기준으로 앞, 뒤
            a = stack_num.pop()             # 전 숫자
            b = int(sen[i])                 # 다음 숫자
            stack_num.append(b * int(a))

        else:                               # 숫자일 경우 숫자 리스트에 담는다
            stack_num.append(sen[i])
        i += 1

    result = 0
    while stack_num:                        # 숫자 리스트안의 모든 숫자를 더한다
        x = stack_num.pop()
        result += int(x)

    print(f'#{tc} {result}')