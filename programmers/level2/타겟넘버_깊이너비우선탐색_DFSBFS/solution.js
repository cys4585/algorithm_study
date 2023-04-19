function solution(numbers, target) {
  let answer = 0

  answer = recursion(numbers, 0, 0, target)

  return answer
}

const recursion = (numbers, idx, value, target) => {
  if (numbers.length === idx) {
    return value === target ? 1 : 0
  }

  let result = 0
  result += recursion(numbers, idx + 1, value + numbers[idx], target)
  result += recursion(numbers, idx + 1, value - numbers[idx], target)

  return result
}

console.log(solution([1, 1, 1, 1, 1], 3)) // 5
console.log(solution([4, 1, 2, 1], 4)) // 2
