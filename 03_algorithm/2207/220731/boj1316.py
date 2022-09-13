result = 0
for _ in range(int(input())):
    word = input()
    cnt = 1
    if len(word) == 1:
        result += 1
    else:
        for i in range(0, len(word) - 1):
            if word[i] == word[i+1]:
                cnt += 1
            else:
                if cnt != word.count(word[i]):
                    break
                else:
                    cnt = 1
        else:
            result += 1
print(result)