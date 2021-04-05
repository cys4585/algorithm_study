# 무한 문자열

def find_repeat(original_str):
    repeat_str = original_str[0]
    i = 1
    while i < len(original_str):
        print(i, original_str[i])
        if repeat_str[0] != original_str[i]:
            repeat_str += original_str[i]
        else:
            flag = False
            for j in range(1, len(repeat_str)):
                if i + j >= len(original_str) or repeat_str[j] != original_str[i + j]:
                    flag = True
                    break
            if flag:
                repeat_str += original_str[i]
            else:
                i = i + len(repeat_str) - 1
        i += 1
        print(repeat_str)
    return repeat_str


s = input()
t = input()
if len(s) > len(t): s, t = t, s

# repeat_str_s = find_repeat(s)
# print(repeat_str_s)
repeat_str_t = find_repeat(t)
print(repeat_str_t)