function solution(n, k) {
  let answer = -1

  const candidates = parse(n, k).split("0")
  answer = candidates.filter((candidate) => isPrime(parseInt(candidate))).length

  return answer
}

const parse = (n, k) => {
  if (n < k) return "" + n
  return "" + parse(Math.floor(n / k), k) + (n % k)
}

const isPrime = (number) => {
  if (isNaN(number) || number < 2) return false

  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i === 0) return false
  }

  return true
}

console.log(solution(1, 9)) // 3
console.log(solution(2, 9)) // 3
console.log(solution(3, 9)) // 3
console.log(solution(4, 9)) // 3
console.log(solution(5, 9)) // 3
console.log(solution(6, 9)) // 3
console.log(solution(7, 9)) // 3
console.log(solution(8, 9)) // 3
console.log(solution(9, 9)) // 3
console.log(solution(10, 9)) // 3
console.log(solution(11, 9)) // 3
console.log(solution(856118, 2)) // 3
console.log(solution(856118, 4)) // 3
console.log(solution(856118, 9)) // 3
console.log(solution(856118, 10)) // 3
console.log(solution(437674, 3)) // 3
console.log(solution(110011, 10)) // 2
