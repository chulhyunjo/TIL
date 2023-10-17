import heapq

COMMAND = ['l', 'r', 'u', 'd']
D = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def solution(n, m, x, y, r, c, k):
    def bfs(x, y):
        pq = [('', x, y, 0)]
        while pq:
            result, x, y, cnt = heapq.heappop(pq)

            # 이동에 필요한 칸
            needmove = abs(x - r) + abs(y - c)
            if needmove > k - cnt: continue
            if abs(k - cnt) % 2 != needmove % 2: continue

            if cnt == k:
                if x == r and y == c:
                    return result
                continue

            for i in range(4):
                dx, dy = D[i]
                nx, ny = x + dx, y + dy
                if 0 >= nx or 0 >= ny or n < nx or m < ny: continue
                heapq.heappush(pq, (result + COMMAND[i], nx, ny, cnt + 1))

        return 'impossible'

    needmove = abs(x - r) + abs(y - c)
    if (k - needmove) % 2 == 1 or needmove > k:
        return 'impossible'

    result = bfs(x, y)
    return result