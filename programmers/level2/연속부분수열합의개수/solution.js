function solution(elements) {
  let answer = 0

  const resultArr = []
  for (let i = 0; i < elements.length; i++) {
    resultArr.push(...calculate(elements, i))
  }

  answer = new Set(resultArr).size
  return answer
}

const calculate = (elements, startIdx) => {
  const result = []

  let value = 0
  for (let i = startIdx; i < startIdx + elements.length; i++) {
    value += elements[i % elements.length]
    result.push(value)
  }
  return result
}

console.log(solution([7, 9, 1, 1, 4])) // 18
