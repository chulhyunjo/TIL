str = ['b','d','p','q']
mirror = ['d','b','q','p']

for tc in range(1, int(input())+1):
    word = input()
    result = ''
    for i in range(len(word)-1, -1, -1):
        result += mirror[str.index(word[i])]
    print(f'#{tc} {result}')
