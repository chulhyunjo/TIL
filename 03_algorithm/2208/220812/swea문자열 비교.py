for tc in range(1, int(input())+1):
    word1 = input()
    word2 = input()
    result = 0
    for i in range(len(word2) - len(word1) + 1):
        if word1 == word2[i:i+len(word1)]:
            result = 1
            break

    print(f'#{tc} {result}')