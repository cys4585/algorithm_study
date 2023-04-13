function solution(s) {
  const answer = []

  const tupleExpression = parseTupleExpression(s)
  tupleExpression.forEach((arr) => {
    answer.push(arr.find((element) => !answer.includes(element)))
  })

  return answer
}

function parseTupleExpression(s) {
  return s
    .split("},{")
    .map((str) => str.split("").filter((c) => !["{", "}"].includes(c)))
    .map((arr) =>
      arr
        .join("")
        .split(",")
        .map((str) => parseInt(str))
    )
    .sort((a, b) => a.length - b.length)
}

console.log(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) // [2, 1, 3, 4]
console.log(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")) // [(2, 1, 3, 4)]
console.log(solution("{{20,111},{111}}")) // [(111, 20)]
console.log(solution("{{123}}")) // [123]
console.log(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) // [(3, 2, 4, 1)]
