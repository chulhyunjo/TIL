word = input()

result = 0
value = 1
stack_1 = [] # () 를 담을 리스트
stack_2 = [] # [] 를 담을 리스트

for i in range(len(word)):
    if word[i] == '(':
        value *= 2
        stack_1.append(word[i])

    elif word[i] == '[':
        value *= 3
        stack_2.append(word[i])

    elif word[i] == ')':
        if stack_1: # stack_1 에 (가 있나 없나
            if word[i-1] == '(':
                result += value
            stack_1.pop()
            value //= 2
        else:
            result = 0
            break

    else:
        if stack_2: #stack_2에 [가 있나 없나
            if word[i-1] == '[':
                result += value
            stack_2.pop()
            value //= 3
        else:
            result = 0
            break
if stack_1 or stack_2: # '(' or '['가 남아 있으면
    print(0)
else:
    print(result)