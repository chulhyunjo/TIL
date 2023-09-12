from collections import Counter

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    word = input().rstrip()
    K = int(input())
    N = len(word)

    cnt = Counter(word)
    if K == 1:
        print(1, 1)
        continue
    if max(cnt.values()) < K:
        print(-1)
        continue

    words = dict()
    for k, v in cnt.items():
        if v >= K:
            words[k] = v

    s = 0
    e = 1
    alpha = [0] * 26
    alpha[ord(word[s])-97] += 1
    alpha[ord(word[e]) - 97] += 1
    min_answer = 10001
    max_answer = 0
    while s < N:
        while s<N and words.get(word[s], 0) < K:
            alpha[ord(word[s]) - 97] -= 1
            s += 1
            if s == e:
                e += 1
                alpha[ord(word[e]) - 97] += 1
            continue

        if word[e] == word[s] and alpha[ord(word[e]) - 97] == K:
            min_answer = min(min_answer, e-s+1)
            max_answer = max(max_answer, e-s+1)
            words[word[s]] = words[word[s]] - 1

            alpha[ord(word[s]) - 97] -= 1
            s += 1

        else:
            e += 1
            alpha[ord(word[e])-97] += 1

