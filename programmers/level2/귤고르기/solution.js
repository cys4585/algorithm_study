function solution(k, tangerine) {
  let answer = 0

  const orangeCountObj = {}
  tangerine.forEach(
    (size) => (orangeCountObj[size] = (orangeCountObj[size] || 0) + 1)
  )

  const arr = Object.values(orangeCountObj).sort((a, b) => b - a)
  for (const cnt of arr) {
    if (k <= 0) break
    k -= cnt
    answer += 1
  }

  return answer
}

solution(6, [1, 3, 2, 5, 4, 5, 2, 3]) //3
solution(4, [1, 3, 2, 5, 4, 5, 2, 3]) //2
solution(2, [1, 1, 1, 1, 2, 2, 2, 3]) //1
