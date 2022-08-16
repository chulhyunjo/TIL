def solution(numbers, hand):
    answer = ''
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    l = 0
    r = 0
    for i in numbers:
        if i in [1, 4, 7, '*']:
            answer += 'L'
            l = i
        elif i in [3, 6, 9, '#']:
            answer += 'R'
            r = i
        else:
            for m in range(4):
                for n in range(3):
                    if arr[m][n] == l:
                        x1, y1 = m, n
                    elif arr[m][n] == r:
                        x2, y2 = m, n
                    elif arr[m][n] == i:
                        x3, y3 = m, n

            disl = abs(x3 + y3 - x1 - y1)
            disr = abs(x3 + y3 - x2 - y2)
            if disl - disr > 0:
                answer += 'R'
                r = i
            elif disl - disr < 0:
                answer += 'L'
                l = i
            else:
                if hand == 'right':
                    answer += 'R'
                    r = i
                else:
                    answer += 'L'
                    l = i
    return answer

print(solution(	[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))