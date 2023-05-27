def solution(users, emoticons):
    answer = []
    discount = [40, 30, 20, 10]
    emoticon = []

    def dfs(d, priceList):
        if len(priceList) == len(emoticons):
            emoticon.append(priceList)
        elif d == 4:
            return
        else:
            for m in range(len(emoticons)):
                dfs(d + 1, priceList + [((emoticons[d] * (100 - discount[m])) // 100, discount[m])])

    dfs(0, [])
    print(emoticon)

    return answer

solution([[40, 10000], [25, 10000]],[7000, 9000])