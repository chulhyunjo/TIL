def solution(name):
    answer = 0
    name = list(name)
    l = len(name)
    if l == 1:
        answer += min(ord(name[0]) - ord('A'), ord('Z') - ord(name[0]) + 1)
        return answer

    else:
        for i in range(l):
            if name[i] == 'A': continue
            right, left = 1, 1

            while name[i - left] == 'A':
                left += 1

            while i + right <= l - 1 and name[i + right] == 'A':
                right += 1

            answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
            answer += left if left < right else right
            name[i] = 'A'
            return answer - 1

solution('JAN')