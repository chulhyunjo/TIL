def solution(user_id, banned_id):
    answer = 0
    answer_dict = dict()

    N = len(user_id)
    B = len(banned_id)

    checked = [0] * N

    def dfs(d, lst):
        nonlocal answer

        if d == B:
            now = str(sorted(lst))
            if answer_dict.get(now, 0):
                return
            else:
                answer_dict[now] = 1
                answer += 1
            return

        banned = banned_id[d]

        for i in range(N):
            if checked[i]: continue
            name = user_id[i]
            if len(name) != len(banned): continue
            flag = 1
            for j in range(len(name)):
                if name[j] == banned[j]:
                    continue
                elif banned[j] == '*':
                    continue
                else:
                    flag = 0
                    break

            if flag:
                checked[i] = 1
                dfs(d + 1, lst + [i])
                checked[i] = 0

    dfs(0, [])
    return answer