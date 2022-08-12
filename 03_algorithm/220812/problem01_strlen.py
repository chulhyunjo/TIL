def strlen(s):
    i = 0
    word = ''
    while s[i] != '\0':
        word += s[i]
        i += 1
    return word

a = ['a','b','c','\0']
print(strlen(a))