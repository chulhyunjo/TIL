N = int(input())
word = input()
words = [input() for _ in range(N-1)]
l = len(word)

Alpha = [0] * 26
for w in word:
    Alpha[ord(w)-65] += 1

answer = 0
for w in words:
    A = [0] * 26
    for w2 in w:
        A[ord(w2) - 65] += 1

    if A == Alpha:
        answer += 1
        continue

    cnt = 0
    cnt2 = 0
    for i in range(26):
        if Alpha[i] > 0:
            A[i] -= Alpha[i]
            if A[i] < 0:
                cnt -= A[i]
            if A[i] > 0:
                cnt2 += A[i]
        elif not Alpha[i] and A[i]:
            cnt2 += A[i]

    if not (cnt > 1 or cnt2 > 1):
        answer += 1

print(answer)