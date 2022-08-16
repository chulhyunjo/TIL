for tc in range(1, int(input())+1):
    word = list(input())
    stack = [word.pop()]
    for i in range(len(word)):
        if stack and stack[-1] == word[-1]:
            stack.pop()
            word.pop()
        else:
            stack.append(word.pop())
    result = ''.join(stack)
    if result:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} Good')
