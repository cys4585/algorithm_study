function solution(citations) {
  for (let h = Math.max(...citations); h >= 0; h -= 1) {
    let cnt = 0
    for (const nbr of citations) if (nbr > h) cnt += 1

    if (cnt === h) {
      return h
    }
  }
}

console.log(solution([3, 0, 6, 1, 5]))
console.log(solution([1, 0, 10, 5, 3, 2, 6, 8]))
