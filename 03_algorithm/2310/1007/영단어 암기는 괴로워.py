import heapq
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

words = dict()
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        words[word] = words.get(word, 0) + 1

answer = []
for k, v in words.items():
    answer.append((-v, -len(k), k))

answer.sort()
for i in answer:
    print(i[2])