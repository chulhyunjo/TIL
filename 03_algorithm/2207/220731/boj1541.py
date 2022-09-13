s = input().split('-')
result = 0
x = s[0].split('+')

for i in x:
    result += int(i)

for i in s[1:]:
    minus = 0

    if '+' in i:
        i = i.split('+')
        for j in i:
            minus += int(j)
    else:
        result -= int(i)

    result -= minus
print(result)