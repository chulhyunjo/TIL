word = input() + ' '
cnt = 1
result = ''
for i in range(len(word)-1):
    al = word[i]
    if word[i] == word[i+1]:
        cnt += 1
    else:
        result += al + str(cnt)
        cnt = 1

print(result)