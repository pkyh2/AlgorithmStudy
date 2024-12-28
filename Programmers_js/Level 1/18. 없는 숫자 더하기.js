function solution(numbers) {
  const sumOneToNine = Array.from({length: 10}, (v, i) => i).reduce((acc, cur) => acc+cur, 0)
  const sumNumbers = numbers.reduce((acc, cur) => acc+cur, 0)

  return sumOneToNine - sumNumbers
}

console.log(solution([1,2,3,4,6,7,8,0]))
console.log(solution([5,8,4,0,6,7,9]))

