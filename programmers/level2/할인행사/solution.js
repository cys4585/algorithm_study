function solution(want, number, discount) {
  let answer = 0

  for (let i = 0; i <= discount.length - 10; i++) {
    if (isCorrespond(discount, i, want, [...number])) answer += 1
  }
  return answer
}

const isCorrespond = (discount, startIdx, want, number) => {
  for (let i = 0; i < 10; i++) {
    const discountProduct = discount[i + startIdx]
    const wantProductIdx = want.indexOf(discountProduct)
    if (wantProductIdx === -1 || number[wantProductIdx] === 0) return false
    number[wantProductIdx] -= 1
  }

  return number.every((nbr) => nbr === 0)
}

console.log(
  solution(
    ["banana", "apple", "rice", "pork", "pot"],
    [3, 2, 2, 2, 1],
    [
      "chicken",
      "apple",
      "apple",
      "banana",
      "rice",
      "apple",
      "pork",
      "banana",
      "pork",
      "rice",
      "pot",
      "banana",
      "apple",
      "banana",
    ]
  )
) // 3

console.log()

console.log(
  solution(
    ["apple"],
    [10],
    [
      "banana",
      "banana",
      "banana",
      "banana",
      "banana",
      "banana",
      "banana",
      "banana",
      "banana",
      "banana",
    ]
  )
) // 0
