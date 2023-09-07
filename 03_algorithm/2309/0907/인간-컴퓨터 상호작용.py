import sys
def input():
    return sys.stdin.readline().rstrip()

word = input()
N = int(input())
word_length = len(word)
cnt_total = []
cnt = [0] * 26

for i in range(word_length):
    cnt[ord(word[i])-97] += 1
    cnt_total.append(cnt[:])

for _ in range(N):
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    a = ord(a) - 97
    if l == 0:
        print(cnt_total[r][a])
    else:
        print(cnt_total[r][a] - cnt_total[l-1][a])