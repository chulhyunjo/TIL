def moooo(a,i):
    global s0
    if len(a) > n:
        print(a)
        print(a[n-1])
        return
    moooo(a + 'm' + 'o'*(i+2)+a, i+1)


s0 = 'moo'
n = int(input())
moooo(s0,1)