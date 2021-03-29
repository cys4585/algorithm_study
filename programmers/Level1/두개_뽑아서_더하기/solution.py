def solution(numbers):
    answer = set()
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            sum_v = numbers[i] + numbers[j]
            answer.add(sum_v)
    return sorted(list(answer))

numbers = [[2,1,3,4,1], [5,0,2,7]]
for nums in numbers:
    print(type(nums))
    print(solution(nums))