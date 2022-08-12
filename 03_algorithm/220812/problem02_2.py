def my_strcmp(s1,s2):
    #  같으면 0, s1이 빠르면 음수, s2가 빠르면 양수
    s1len = len(s1)
    s2len = len(s2)
    i = 0
    while i < s1len and i < s2len:
        if s1[i] != s2[i]:
            return ord(s1[i]) - ord(s2[i])
        i += 1
    # 같은 경우, 한쪽이 짧은 경우
    return s1len - s2len

print(my_strcmp('abc', 'adc'))
print(my_strcmp('abc', 'aac'))
print(my_strcmp('abc', 'abc'))