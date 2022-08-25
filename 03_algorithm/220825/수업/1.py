string = input()[::-1]
stack = []
digit = []
close_idx = []
temp = 0

for i in range(len(string)):
    s = string[i]

    if s == ')':
        close_idx.append(i)
        stack.append(s)

    elif s == '(':
        prev = 0
        while prev != ')':
            prev = stack.pop()
            temp += len(prev)

        a = close_idx.pop()
        check = string[a:i].count('(')

        for j in range(check):
            try:
                temp += digit.pop()
            except IndexError:
                break
    elif temp:
        digit.append((temp - 1) * int(s))
        temp = 0

    else:
        stack.append(s)

print(len(stack) + sum(digit))
print(stack, digit)