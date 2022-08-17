for tc in range(1, int(input())+1):
    word = list(input())
    stack = []

    while word:
        stack.append(word.pop())
        
        while stack and word and stack[-1] == word[-1]:
            stack.pop()
            word.pop()

    print(f'#{tc} {len(stack)}')