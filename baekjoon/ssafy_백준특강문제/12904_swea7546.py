# A와 B

# A와 B로만 존재하는 단어
# 두 문자열 S, T 주어졌을 때,
# S를 T로 바꿀 수 있는지 판단
# 바꿀 수 있는 연산 2가지
    # 1. 문자열의 뒤에 A를 추가
    # 2. 문자열을 뒤집고 뒤에 B를 추가

def function(s, t):
    global possible
    # print(s)
    if len(s) == len(t):
        if s == t:
            possible = True
        return
    function(s + 'A', t)
    reverse_s = ''
    for i in range(len(s) - 1, -1, -1):
        reverse_s += s[i]
    function(reverse_s + 'B', t)

S = input()
T = input()
possible = False
function(S, T)
if possible:
    print(1)
else:
    print(0)