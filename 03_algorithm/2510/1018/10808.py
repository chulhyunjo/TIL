S = input()
count = [0 for i in range(26)]
for s in S:
    count[ord(s) - ord('a')] += 1

print(*count)