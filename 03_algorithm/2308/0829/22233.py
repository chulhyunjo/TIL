import sys
def solution(N, memo, write):
    input = sys.stdin.readline
    cnt = N
    for words in write:
        for w in words:
            if memo.get(w,0):
                del memo[w]
                cnt -= 1
        print(cnt)

if __name__ == '__main__':
    N, M = map(int, input().split())
    memo = {input().rstrip():1 for _ in range(N)}
    write = [input().rstrip().split(',') for _ in range(M)]
    solution(N, memo, write)