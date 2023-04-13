function solution(arr1, arr2) {
  const answer = []

  const newArr2 = swapRowAndCol(arr2)
  for (let i = 0; i < arr1.length; i++) {
    const calculatedRow = calculateRow(arr1[i], newArr2)
    answer.push(calculatedRow)
  }

  return answer
}

function swapRowAndCol(arr) {
  const result = []

  for (let i = 0; i < arr[0].length; i++) {
    const tmp = []
    for (let j = 0; j < arr.length; j++) tmp.push(arr[j][i])
    result.push(tmp)
  }

  return result
}

function calculateRow(row, arr) {
  const result = []

  for (let i = 0; i < arr.length; i++) {
    let value = 0
    for (let j = 0; j < arr[i].length; j++) value += arr[i][j] * row[j]
    result.push(value)
  }

  return result
}

console.log(
  solution(
    [
      [1, 4],
      [3, 2],
      [4, 1],
    ],
    [
      [3, 3],
      [3, 3],
    ]
  )
) // [ [15, 15], [15, 15], [15, 15] ]

console.log(
  solution(
    [
      [2, 3, 2],
      [4, 2, 4],
      [3, 1, 4],
    ],
    [
      [5, 4, 3],
      [2, 4, 1],
      [3, 1, 1],
    ]
  )
) // [ [22, 22, 11], [36, 28, 18], [29, 20, 14] ]
