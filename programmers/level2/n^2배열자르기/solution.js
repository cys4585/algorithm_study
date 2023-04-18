function solution(n, left, right) {
  const answer = []

  for (let i = left; i <= right; i++) {
    const quotient = Math.floor(i / n)
    const remainder = i % n
    answer.push(1 + (quotient > remainder ? quotient : remainder))
  }

  return answer
}

console.log(solution(3, 2, 5))
console.log(solution(4, 7, 14))
