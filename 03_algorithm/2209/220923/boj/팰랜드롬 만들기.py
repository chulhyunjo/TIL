word = input()
wordDict = {}
n = len(word)
for i in sorted(word):
    wordDict[i] = wordDict.get(i,0) + 1
odd = []
for k,v in wordDict.items():
    if v%2:
        odd.append(k)
    if len(odd)>1:
        print("I'm Sorry Hansoo")
        exit()

result = ['']*(n//2)
idx = 0
for k, v in wordDict.items():
    result[idx:idx+(v//2)] = [k] * (v//2)
    idx += v//2
if odd:
    result = result + [odd[0]] + list(reversed(result))
else:
    result += list(reversed(result))
print(''.join(result))