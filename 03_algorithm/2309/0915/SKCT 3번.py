def solution1(acts):
    answer = []
    backStack, frontStack = [], []
    page, idx = 0, 0

    for act, cnt in acts:
        # 페이지 이동
        if act == 0:
            for c in range(cnt):
                backStack.append(page)
                idx += 1
                page = idx
            frontStack = []

        elif act == -1:
            for c in range(cnt):
                if backStack:
                    frontStack.append(page)
                    page = backStack.pop()
                else:
                    break

        else:
            for c in range(cnt):
                if frontStack:
                    backStack.append(page)
                    page = frontStack.pop()
                else:
                    break


        answer.append(page)
    return answer

def solution2(acts):
    answer = []
    backStack, frontStack = [], []
    page, idx = 0, 0
    for act, cnt in acts:
        # 페이지 이동
        if act == 0:
            if idx == page:
                backStack.append([idx, idx+cnt-1])
            else:
                backStack.append([page, page])
                backStack.append([idx+1, idx+cnt-1])
            frontStack = list()
            idx += cnt
            page = idx

        # 앞으로
        if act == 1:
            tmp = cnt
            while frontStack and tmp:
                first, last = frontStack[-1]
                # 범위 안이면
                if first - last + 1 > tmp:
                    if page == idx:
                        backStack.append([page, page+tmp-1])
                    else:
                        backStack.append([page, page])
                        backStack.append([last, last+tmp-2])
                    frontStack[-1][1] += tmp
                    page = frontStack[-1][1] - 1
                    break
                elif first - last + 1 == tmp:
                    backStack.append([frontStack[-1][1], frontStack[-1][0]-1])
                    frontStack.pop()
                    page = backStack[-1][1] + 1
                else:
                    num_cnt = first - last + 1
                    tmp -= num_cnt
                    if page == idx:
                        frontStack[-1][0] -= 1
                        backStack.append([frontStack[-1][1], frontStack[-1][0]])
                        page = backStack[-1][1] + 1
                    else:
                        backStack.append([page, page])
                        if frontStack[-1][1] == frontStack[-1][0]:
                            page = frontStack[-1][1]
                        elif first - last + 1 == tmp:
                            backStack.append([frontStack[-1][1], frontStack[-1][0] - 1])
                            frontStack.pop()
                            page = backStack[-1][1] + 1
                        else:
                            backStack.append([frontStack[-1][1], frontStack[-1][0]])
                            page = frontStack[-1][1] + 1
                        frontStack.pop()
        # 뒤로
        if act == -1:
            tmp = cnt
            while backStack and tmp:
                first, last = backStack[-1]
                # 범위 안이면
                if last - first + 1 > tmp:
                    if page == idx:
                        frontStack.append([page, page-tmp+1])
                    else:
                        frontStack.append([page, page])
                        frontStack.append([last, last-tmp+2])
                    backStack[-1][1] -= tmp
                    page = backStack[-1][1] - 1
                    break
                else:
                    num_cnt = last - first + 1
                    tmp -= num_cnt
                    if page == idx:
                        backStack[-1][0] += 1
                        frontStack.append([page, backStack[-1][0]])
                        page = frontStack[-1][1] - 1
                    else:
                        frontStack.append([page, page])
                        if backStack[-1][1] == backStack[-1][0]:
                            page = backStack[-1][1]
                        elif last - first + 1 == tmp:
                            frontStack.append([backStack[-1][1], backStack[-1][0] - 1])
                            backStack.pop()
                            page = frontStack[-1][0] + 1
                        else:
                            frontStack.append([backStack[-1][1], backStack[-1][0]])
                            page = backStack[-1][0] - 1
                    backStack.pop()
        answer.append(page)
    return answer

if __name__ == '__main__':
    # acts = [[0, 48], [-1, 52], [1, 10], [0, 10], [-1, 20], [0, 3], [-1, 99], [1, 3], [0, 2], [0, 10]]
    acts = [[0, 480000000], [-1, 520000000], [1, 100000000], [0, 100000000], [-1, 200000000], [0, 30000000], [-1, 990000000], [1, 30000000], [0, 20000000], [0, 100000000]]
    # [48, 0, 10, 58, 0, 61, 0, 61, 63, 73]
    # acts = [[0, 1000000000], [-1, 100000000], [1, 1000000000], [-1, 1000000000], [1, 1000000000], [-1, 1000000000], [0, 1000000000]]
    # print(solution1(acts))
    print(solution2(acts))