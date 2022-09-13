for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int,input().split()))
    stack = []
    result = 0
    for i in range(1, n):
        stack.append(arr.pop())

        while stack and stack[0] < arr[-1]:
            stack.pop()

        if stack:
            result += stack[0] - arr[-1]

    print(f'#{tc} {result}')