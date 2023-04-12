const pair = {
  "{": "}",
  "[": "]",
  "(": ")",
}
const openingBrackets = ["(", "[", "{"]
const closingBrackets = [")", "]", "}"]

function solution(s) {
  let answer = 0

  for (let x = 0; x < s.length; x++) {
    let movedStr = moveLeft(s, x)
    if (checkCorrectStr(movedStr)) answer += 1
  }
  return answer
}

function moveLeft(s, x) {
  return s.substring(x) + s.substring(x - s.length, x)
}

function checkCorrectStr(s) {
  const stack = []

  for (let i = 0; i < s.length; i++) {
    let currentBracket = s[i]
    if (openingBrackets.includes(currentBracket)) stack.push(currentBracket)
    else {
      const latestBracket = stack.pop()
      if (pair[latestBracket] !== currentBracket) {
        return false
      }
    }
  }

  if (stack.length > 0) return false

  return true
}

console.log(solution("[](){}")) // 3
console.log(solution("}]()[{")) // 2
console.log(solution("[)(]")) // 0
console.log(solution("}}}")) // 0
console.log(solution("{(())[{}]}")) // 1
