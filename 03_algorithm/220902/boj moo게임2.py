s0 = 3
cnt = 1
n = int(input())
s = [s0]
while s0 < n:
    s0 += s0 + (cnt + 3)
    cnt += 1
    s.append(s0)
for q in range(cnt-1,0,-1):
    mid = s[q] - s[q-1] * 2
    if s[q-1] > n:
        continue
    if n - s[q-1]<=mid:
        n -= s[q-1]
        break
    else:

        n -= (s[q-1] + mid)

if not n-1:
    print('m')
else:
    print('o')