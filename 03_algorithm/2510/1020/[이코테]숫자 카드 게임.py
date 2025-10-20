"""
입력
3 3
3 1 2
4 1 4
2 2 2

출력
2

입력
2 4
7 3 1 8
3 3 3 4

출력
3
"""

N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]
cards = list(map(lambda x: min(x), cards))
print(max(cards))