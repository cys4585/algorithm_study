function solution(progresses, speeds) {
  const answer = []

  let deployCnt = 0
  let deployIdx = 0
  while (deployIdx < progresses.length) {
    work(deployIdx, progresses, speeds)
    deployCnt = countCanDeploy(deployIdx, progresses)
    if (deployCnt === 0) continue
    deployIdx += deployCnt
    answer.push(deployCnt)
  }
  return answer
}

const work = (idx, progresses, speeds) => {
  for (let i = idx; i < progresses.length; i++) {
    if (progresses[i] >= 100) continue
    progresses[i] += speeds[i]
  }
}

const countCanDeploy = (idx, progresses) => {
  let cnt = 0

  for (let i = idx; i < progresses.length; i++) {
    if (progresses[i] < 100) break
    cnt++
  }
  return cnt
}

console.log(solution([93, 30, 55], [1, 30, 5])) // [2, 1]
console.log(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) // [1, 3, 2]
