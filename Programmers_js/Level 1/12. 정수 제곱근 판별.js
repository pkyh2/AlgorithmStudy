function solution(n) {
  let valueSqrt = Math.sqrt(n)
  let isSquare = Number.isInteger(valueSqrt)
  if (isSquare) {
    return Math.pow(valueSqrt+1, 2)
  } else {
    return -1
  }
}

console.log(solution(121))
console.log(solution(3))