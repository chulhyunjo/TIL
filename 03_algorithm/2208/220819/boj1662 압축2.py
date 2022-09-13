word = input()
l = 0
stack = []
for i in word:
    if i.isdigit():
        l += 1
        K = i
    elif i == '(':
        stack.append((K, l-1)) # 곱:k, 길이
        l = 0

    elif i == ')':
        m, result_l = stack.pop()
        l = l * int(m) + result_l
print(l)