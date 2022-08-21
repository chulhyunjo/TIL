n = int(input())
answer = 0
rows = [0] * n # 현재 놓은 퀸 자리가 유효한지 체크
def is_valid(r):
    for i in range(r):        # 세로 체크
        if rows[i] == rows[r]:
            return False
        if abs(r - i) == abs(rows[r] - rows[i]):
            return False
    return True


def put_queen(r):
    global answer
    if r == n:
        answer += 1
        return

    for i in range(n):
        rows[r] = i
        if is_valid(r):
            put_queen(r + 1)
put_queen(0)
print(answer)
