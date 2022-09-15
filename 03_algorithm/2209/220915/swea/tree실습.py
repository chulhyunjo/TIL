def pre(i):     # 전위 순회로 사칙연산 식 담기
    if i:
        result.append(tree[i])
        pre(ch1[i])
        pre(ch2[i])

for tc in range(1, 11):
    N = int(input())
    tree = [''] * (N+1) # 트리 생성
    ch1 = [0] * (N+1)   # 자식1
    ch2 = [0] * (N+1)   # 자식2

    for _ in range(N):
        node, n, *c = input().split()
        node = int(node)
        if c:           # 자식이 있다면 담기
            c = list(map(int, c))
            ch1[node] = c[0]
            ch2[node] = c[1]
        tree[node] = n  # 트리에 현재 값 저장
    result = []         # 사칙 연산 담을 리스트
    pre(1)
    stack = []          # 임시 저장 스택
    print(result)
    while result:       # 사칙 연산이 끝날 때까지 실행
        x = result.pop()    # 1개 pop
        if x.isnumeric():   # 숫자면 임시 스택에 저장
            stack.append(int(x))
        else:           # 아니라면 임시 저장한 숫자 사칙연산
            a = stack.pop()
            b = stack.pop()
            if x == '+':
                stack.append(a+b)
            if x == '-':
                stack.append(a-b)
            if x == '/':
                stack.append(a/b)
            if x == '*':
                stack.append(a*b)
    print(f'#{tc} {stack[0]:.0f}')  # 정수만 출력