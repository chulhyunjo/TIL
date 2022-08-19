n = int(input())                # 피연산자의 개수
word = list(input())            # 후위표기식
valAl = [0] * n                 # 영문자가 나타내는 값을 저장할 리스트
for i in range(n):
    valAl[i] = int(input())     # A~Z 순서대로 입력된다고 함

num_s = []                      # 임시 저장할 리스트
for i in word:
    if i.isalpha():             # i가 문자일 경우
        num_s.append(valAl[ord(i) -65]) # i가 나타내는 값을 임시 저장 리스트(num_s)에 삽입
    else:
        if i == '*':            # 연산자인 경우
            a = num_s.pop()     # 뒤에 들어간 값들부터 계산해야 하므로 2개를 pop한다
            b = num_s.pop()     # 2개의 숫자중에 먼저 들어간 숫자가 b, 늦게 들어간 숫자가 a
            res = b * a         # 연산은 -> b - a, b + a, b * a, b / a로 한다
            num_s.append(res)   # 연산된 값은 다시 임시 저장 리스트(num_s)에 저장
        elif i == '-':
            a = num_s.pop()
            b = num_s.pop()
            res = b - a
            num_s.append(res)
        elif i == '+':
            a = num_s.pop()
            b = num_s.pop()
            res = b + a
            num_s.append(res)
        elif i == '/':
            a = num_s.pop()
            b = num_s.pop()
            res = b / a
            num_s.append(res)
print(f'{num_s[0]:.2f}')

'''
후위 표기식은 
111++ -> (1+(1+1))
123*+ -> (1+(2*3))
뒤에 입력된 숫자 2개를 먼저 앞에 있는 연산자로 연산한다. 
'''