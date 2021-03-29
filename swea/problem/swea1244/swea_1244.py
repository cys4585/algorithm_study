# 최대 상금
# D3
import sys
sys.stdin = open("input_1244.txt")

def function(nums, cnt):
    global max_v
    # print(nums, cnt)
    if cnt == total_change or cnt == len(nums) // 2 + 1:
        if cnt == len(nums) // 2 + 1:
            while cnt < total_change:
                cnt += 1
                nums[-1], nums[-2] = nums[-2], nums[-1]
        val = 0
        for i in range(len(nums)):
            val += nums[i] * 10 ** (len(nums) - 1 - i)
        if max_v < val: max_v = val
        return
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            function(nums, cnt+1)
            nums[i], nums[j] = nums[j], nums[i]


for tc in range(1, int(input()) + 1):
    numbers, total_change = input().split()
    numbers = list(map(int, numbers))
    total_change = int(total_change)
    # print(numbers, total_change)

    max_v = 0
    function(numbers, 0)
    print("#{} {}".format(tc, max_v))