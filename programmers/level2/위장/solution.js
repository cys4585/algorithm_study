function solution(clothes) {
  let answer = 0

  const clotheObj = {}
  clothes.forEach(([name, kind]) => {
    if (!(kind in clotheObj)) clotheObj[kind] = []
    clotheObj[kind].push(name)
  })
  console.log(clotheObj)

  answer =
    Object.values(clotheObj)
      .map((arr) => arr.length + 1)
      .reduce((accumulator, currentValue) => accumulator * currentValue, 1) - 1
  return answer
}

console.log(
  solution([
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
  ])
) // 5

console.log(
  solution([
    ["crow_mask", "face"],
    ["blue_sunglasses", "face"],
    ["smoky_makeup", "face"],
  ])
) // 3
