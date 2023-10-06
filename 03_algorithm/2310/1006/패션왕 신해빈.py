import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    fashion = dict()

    for _ in range(N):
        a, b = input().rstrip().split()
        fashion[b] = fashion.get(b, []) + [a]

    answer = 1
    for v in fashion.values():
        answer *= len(v)+1

    print(answer - 1)