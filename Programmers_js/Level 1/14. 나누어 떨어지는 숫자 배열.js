function solution(arr, divisor) {
  let answer = arr.filter((v) => v % divisor === 0)
  if (answer.length === 0) {
    answer.push(-1)
  } else {
    answer.sort((a, b) => a - b)
  }
  return answer
}

console.log(solution([5, 9, 7, 10], 5))
console.log(solution([2, 36, 1, 3], 1))
console.log(solution([3, 2, 6], 10))