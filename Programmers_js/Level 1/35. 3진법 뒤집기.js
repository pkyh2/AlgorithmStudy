function solution(n) {
  return parseInt(n.toString(3).split('').reverse().join(''), 3)
}

// 1. 

console.log(solution(45))
console.log(solution(125))