function solution(k, dungeons) {
  let answer = -1

  const values = []
  dungeons = dungeons.map((arr) => [...arr, false])

  recursion(k, dungeons, values, 0)

  answer = Math.max(...values)
  return answer
}

const recursion = (k, dungeons, values, cnt) => {
  if (dungeons.every(([a, b, check]) => check)) {
    values.push(cnt)
    return
  }

  for (let i = 0; i < dungeons.length; i++) {
    if (dungeons[i][2]) continue

    let currK = k
    let currCnt = cnt
    if (k >= dungeons[i][0]) {
      currK -= dungeons[i][1]
      currCnt += 1
    }
    dungeons[i][2] = true
    recursion(currK, dungeons, values, currCnt)
    dungeons[i][2] = false
  }
}

console.log(
  solution(80, [
    [80, 20],
    [50, 40],
    [30, 10],
  ])
) // 3
