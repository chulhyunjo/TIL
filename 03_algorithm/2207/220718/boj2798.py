from itertools import combinations

n, m = map(int, input().split())

lst = list(map(int, input().split()))
summ = []

# 여러 카드중 3개만 고르기 combinations(lst, 3)
for cards in combinations(lst, 3):
    summ_card = sum(cards)
    summ.append(summ_card)

for i in range(len(summ)):
    if summ[i] > m:
        summ[i] = 0

print(max(summ))