ps = input()
cnt = 0
result = 0
for idx, bracket in enumerate(ps[:len(ps)-1]):
    if bracket == '(':
        if ps[idx + 1] == '(':
            cnt += 1
        else:
            result += cnt

    else:
        if ps[idx + 1] == ')':
            cnt -= 1
            result += 1

print(result)
