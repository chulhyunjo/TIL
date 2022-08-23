for tc in range(1,int(input())+1):
    inp = list(input().split())
    s = []                              # 숫자를 담을 리스트
    op = ['+', '-', '*', '/']           # 연산자 목록
    result = 0                          # 결과 값
    for i in inp:                       # 하나씩 확인
        if i == '.':                    # '.' 이면 종료
            result = s.pop()            # '.'이 나오면 마지막 결과값 얻기
            break

        elif i in op:
            if len(s) < 2:              # 안의 숫자가 2개가 아니면 연산 x
                result = 'error'
                break
            a = int(s.pop())
            b = int(s.pop())
            if i == '+':
                s.append(b+a)

            if i == '-':
                s.append(b-a)

            if i == '*':
                s.append(b*a)

            if i == '/':
                s.append(b//a)
        else:                           # 숫자는 숫자 리스트에 담기
            s.append(i)

    if s:
        result = 'error'                # 안에 숫자가 또 있을 경우 
    print(f'#{tc} {result}')