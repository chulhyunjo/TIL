for tc in range(1, int(input())+1):
    word = list(input())            # 문자 입력
    stack = []                      # 문자열을 담을 스택

    while word:
        stack.append(word.pop())    # 스택에 word의 끝자리 push
        
        while stack and word and stack[-1] == word[-1]:
            # 스택의 마지막 자리와 word의 마지막자리가 같으면 계속 실행
            stack.pop()             # 같으면 stack, word의 같은 문자를 없앤다(pop)
            word.pop()

    print(f'#{tc} {len(stack)}')    # 남은 문자열의 길이를 출력