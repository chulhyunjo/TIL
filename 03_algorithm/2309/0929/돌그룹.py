from collections import deque

def bfs():
    queue = deque()
    queue.append((A, B, C))
    visited.add((A, B, C))
    while queue:
        a, b, c = queue.popleft()
        if a == b == c:
            return 1

        if a != b:
            if a > b:
                na = a - b
                nb = b * 2
            else:
                na = a * 2
                nb = b - a
            if not (na, nb, c) in visited:
                visited.add((na,nb,c))
                queue.append((na,nb,c))

        if b != c:
            if b > c:
                nb = b - c
                nc = c * 2
            else:
                nb = b * 2
                nc = c - b
            if not (a, nb, nc) in visited:
                visited.add((a,nb,nc))
                queue.append((a,nb,nc))

        if a != c:
            if a > c:
                na = a - c
                nc = c * 2
            else:
                na = a * 2
                nc = c - a
            if not (na, b, nc) in visited:
                visited.add((na,b,nc))
                queue.append((na,b,nc))
    return 0

A, B, C = map(int,input().split())
visited = set()

print(bfs())
