function solution(str1, str2) {
  let answer = 0

  const multiSet1 = makeMultiSet(str1)
  const multiSet2 = makeMultiSet(str2)

  if (multiSet1.length === 0 && multiSet2.length === 0) return 65536

  const intersection = extractIntersection([...multiSet1], [...multiSet2])
  const union = extractUnion([...multiSet1], [...multiSet2])

  answer = intersection.length / union.length

  return Math.floor(answer * 65536)
}

const makeMultiSet = (str) => {
  return str
    .split("")
    .map((c1, idx, arr) => {
      if (arr.length - 1 === idx) return
      const c2 = arr[idx + 1]
      if (
        c1.toLowerCase() === c1.toUpperCase() ||
        c2.toLowerCase() === c2.toUpperCase()
      )
        return

      const element = (c1 + c2).toLowerCase()
      return element
    })
    .filter((element) => element)
}

const extractIntersection = (multiSet1, multiSet2) => {
  const intersection = []

  for (const el of multiSet1) {
    if (multiSet2.includes(el)) {
      intersection.push(el)
      multiSet2.splice(multiSet2.indexOf(el), 1)
    }
  }

  return intersection
}

const extractUnion = (multiSet1, multiSet2) => {
  const union = []

  for (const el of multiSet1) {
    union.push(el)
    if (multiSet2.includes(el)) multiSet2.splice(multiSet2.indexOf(el), 1)
  }

  for (const el of multiSet2) {
    union.push(el)
  }

  return union
}

console.log(solution("FRANCE", "french")) // 16384
console.log(solution("handshake", "shake hands")) // 65536
console.log(solution("aa1+aa2", "AAAA12")) // 43690
console.log(solution("E=M*C^2", "e=m*c^2")) // 65536
