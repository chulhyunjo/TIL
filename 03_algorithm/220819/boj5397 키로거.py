for _ in range(int(input())):
    word = list(input())
    stack = []                              # 방향키를 사용하면 잠시 저장해둘 공간
    result = []                             # 결과값을 담을 리스트

    for i in word:
        if result and i == '<':             # 현재 '<'(왼쪽 방향키)일 경우
                                            # 입력된 값(result)가 있는 경우만 실행
            stack.append(result.pop())      # 임시 저장할 공간에 커서 오른쪽 문자 저장

        if stack and i == '>':              # 현재 '>'(오른쪽 방향키)일 경우
                                            # 임시저장한 값(stack)가 있는 경우만 실행
            result.append(stack.pop())      # 임시 저장한 문자 1개를 입력값에 넣는다.

        if result and i == '-':             # 입력된 값이 있고 '-'(백스페이스)누르면
            result.pop()                    # 입력된 값 하나 삭제

        if i.isalnum():                     # 영어, 숫자일 경우
            result.append(i)                # 입력하기

    while stack:                            # 끝나고 임시저장한 문자 입력값에 넣기
        result.append(stack.pop())

    print(''.join(result))