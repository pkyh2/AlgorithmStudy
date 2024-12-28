function solution(a, b) {
  var answer = 2*a*b > Number(`${a}${b}`) ? 2*a*b : Number(`${a}${b}`)
  return answer;
}

console.log(solution(2, 91))
console.log(solution(91, 2))