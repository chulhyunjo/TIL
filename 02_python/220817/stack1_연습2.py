# 여는 괄호 push
# 닫는 괄호 pop
# 더이상 괄호가 없을 때, 스택이 비어있으면 정상, 스택에 남은게 있으면 에러
T = int(input())
for tc in range(1, T+1):
    a = input()
    s = []
    answer = 1
    for i in a:
        if i == '(':
            s.append(i)
        elif i == ')':
            if s:
                s.pop()
            else:
                answer = 0
                break
    else:
        answer = 0 if s else 1
    print(f'#{tc} {answer}')