def dfs(now_idx, cost, merged):
    global result
    if cost >= result: return

    if now_idx == n:
        if can_merge(merged):
            result = min(result, cost)
        return

    dfs(now_idx + 1, cost, merged) # 안삼

    dfs(now_idx + 1, cost + int(books[now_idx][0]), merged + books[now_idx][1]) # 삼


def check_count(x):
    count = [0] * 27
    for i in x:
        count[ord(i)-65] += 1
    return count

def can_merge(merged):
    merge = check_count(merged)
    word_tmp = word[:]

    for i in range(27):
        if word_tmp[i] > 0:
            word_tmp[i] -= merge[i]
    if all(x <= 0 for x in word_tmp): return True
    else: return False


word = check_count(input())
n = int(input())

books = [input().split() for _ in range(n)]

result = float('inf')

dfs(0, 0, "")
print(result if result != float('inf') else -1)