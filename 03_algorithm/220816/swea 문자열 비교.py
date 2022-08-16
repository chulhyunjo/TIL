for tc in range(1, int(input())+1):
    word1 = input()
    word2 = input()
    n = len(word1)
    m = len(word2)
    result = 0

    for i in range(m-n+1):
        check = word2[i:i+n]
        if check == word1:
            result = 1

    print(f'#{tc} {result}')