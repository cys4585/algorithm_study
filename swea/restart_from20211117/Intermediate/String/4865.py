import sys
sys.stdin = open('./4865_sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    char_dict = {}
    for c in set(str1):
        char_dict[c] = 0

    for c in str2:
        if c in char_dict:
            char_dict[c] += 1
    values = char_dict.values()
    print(f'#{tc} {max(values)}')