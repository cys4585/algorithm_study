# A -> B

def operate(a, b, cnt):
    global min_cnt
    if a >= b:
        if a == b:
            if min_cnt == -1 or min_cnt > cnt:
                min_cnt = cnt
        return
    operate(a*2, b, cnt+1)
    operate(int(str(a) + str(1)), b, cnt+1)


A, B = map(int, input().split())
min_cnt = -1
operate(A, B, 1)

print(min_cnt)