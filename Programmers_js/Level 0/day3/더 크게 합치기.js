
function solution(a, b) {
  var answer = 0;
  const sum1 = parseInt(String(a) + String(b)) // `${a}${b}`
  const sum2 = parseInt(String(b) + String(a)) // `${b}${a}`
  answer = sum1 > sum2 ? sum1 : sum2
  return answer;
}

console.log(solution(9, 91))
console.log(solution(89, 8))