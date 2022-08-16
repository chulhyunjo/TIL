for tc in range(1, int(input())+1):
    word = list(input())
    stack = []
    for _ in range(len(word)):
        x = word.pop()
        if x in stack:
            stack.pop(stack.index(x))
        else:
            stack.append(x)

    if stack:
        print(f'#{tc} {"".join(sorted(stack))}')
    else:
        print(f'#{tc} Good')