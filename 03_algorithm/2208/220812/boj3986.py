n = int(input())
result = 0

for _ in range(n):
    word = input()
    if word.count('A') % 2 or word.count('B') % 2:
        continue
    stack = [word[0]]
    for i in range(1, len(word)):
        if stack:
            last_word = stack[-1]
            if last_word == word[i]:
                stack.pop()
            else:
                stack.append(word[i])
        else:
            stack.append(word[i])
    if not stack:
        result += 1

print(result)