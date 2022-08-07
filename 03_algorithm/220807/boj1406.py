import sys
word = list(input())
n = int(input())
stack = []

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'P':
        word.append(command[1])
    if command[0] == 'L':
        if not word: continue
        x = word.pop()
        stack.append(x)

    if command[0] == 'D':
        if not stack: continue
        x = stack.pop()
        word.append(x)

    if command[0] == 'B':
        if not word: continue
        else: word.pop()

if stack:
    stack.reverse()
    word += stack

print(''.join(word))