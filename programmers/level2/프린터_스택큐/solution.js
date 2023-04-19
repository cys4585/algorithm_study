function solution(priorities, location) {
  let answer = 0

  priorities = changeStructure(priorities, location)

  let cnt = 0
  while (priorities.length) {
    const priority = priorities.shift()

    if (checkMax(priority.doc, priorities)) {
      cnt++
      if (priority.target) {
        answer = cnt
        break
      }
    } else {
      priorities.push(priority)
    }
  }
  return answer
}

const changeStructure = (priorities, location) => {
  return (priorities = priorities.map((doc, idx) => ({
    doc,
    target: location === idx,
  })))
}

const checkMax = (doc, priorities) => {
  return priorities.every((priority) => doc >= priority.doc)
}

console.log(solution([2, 1, 3, 2], 2)) // 1
console.log(solution([1, 1, 9, 1, 1, 1], 0)) // 5
