from collections import deque


def solution(a, b, c, d):
    def bfs(a, b, c):
        while queue:
            now_a, now_b, now_c, cnt = queue.popleft()
            if now_a == d or now_b == d or now_c == d:
                return cnt

            # a 가득 채우기
            if now_a < a and not (a, now_b, now_c) in check:
                queue.append((a, now_b, now_c, cnt + 1))
                check.add((a, now_b, now_c))

            if now_a:
                # 버리기
                if not (0, now_b, now_c) in check:
                    queue.append((0, now_b, now_c, cnt + 1))
                    check.add((0, now_b, now_c))
                # a-> b
                if now_b != b:
                    need = min(now_a, b - now_b)
                    if not (now_a - need, now_b + need, now_c) in check:
                        queue.append((now_a - need, now_b + need, now_c, cnt + 1))
                        check.add((now_a - need, now_b + need, now_c))
                # a-> c
                if now_c != c:
                    need = min(now_a, c - now_c)
                    if not (now_a - need, now_b, now_c + need) in check:
                        queue.append((now_a - need, now_b, now_c + need, cnt + 1))
                        check.add((now_a - need, now_b, now_c + need))

            # b 가득 채우기
            if now_b < b and not (now_a, b, now_c) in check:
                queue.append((now_a, b, now_c, cnt + 1))
                check.add((now_a, b, now_c, cnt + 1))

            if now_b:
                # 버리기
                if not (now_a, 0, now_c) in check:
                    queue.append((now_a, 0, now_c, cnt + 1))
                    check.add((now_a, 0, now_c))
                # b-> a
                if now_a != a:
                    need = min(now_b, a - now_a)
                    if not (now_a + need, now_b - need, now_c) in check:
                        queue.append((now_a + need, now_b - need, now_c, cnt + 1))
                        check.add((now_a + need, now_b - need, now_c))
                # b-> c
                if now_c != c:
                    need = min(now_b, c - now_c)
                    if not (now_a, now_b - need, now_c + need) in check:
                        queue.append((now_a, now_b - need, now_c + need, cnt + 1))
                        check.add((now_a, now_b - need, now_c + need))
            # c가득 채우기
            if now_c < c and not (now_a, now_b, c) in check:
                queue.append((now_a, now_b, c, cnt + 1))
                check.add((now_a, now_b, c, cnt + 1))
            if now_c:
                # 버리기
                if not (now_a, now_b, 0) in check:
                    queue.append((now_a, now_b, 0, cnt + 1))
                    check.add((now_a, now_b, 0))
                # c-> a
                if now_a != a:
                    need = min(now_c, a - now_a)
                    if not (now_a + need, now_b, now_c - need) in check:
                        queue.append((now_a + need, now_b, now_c - need, cnt + 1))
                        check.add((now_a + need, now_b, now_c - need))
                # c-> b
                if now_b != b:
                    need = min(now_c, b - now_b)
                    if not (now_a, now_b + need, now_c - need) in check:
                        queue.append((now_a, now_b + need, now_c - need, cnt + 1))
                        check.add((now_a, now_b + need, now_c - need))

        return -1

    check = set()
    queue = deque([(0, 0, 0, 0)])
    return bfs(a, b, c)