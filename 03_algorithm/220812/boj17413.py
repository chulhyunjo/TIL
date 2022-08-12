sentence = list(input()) + [' ']
stack = []
new_sentence = ''
sentence.reverse()

while sentence:
    x = sentence.pop()
    if x != ' ' and x != '<':
        stack.append(x)

    elif x == ' ':
        while stack:
            new_sentence += stack.pop()
        new_sentence += x
    elif x == '<':
        while stack:
            new_sentence += stack.pop()
        new_sentence += x
        while x != '>':
            x = sentence.pop()
            new_sentence += x

print(new_sentence)