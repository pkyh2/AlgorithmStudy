function solution(n, k) {
  var answer = [];
  let i = 1
  let sum = k;
  while (sum <= n) {
    answer.push(k * i)
    i++
    sum += k
  }
  return answer;
}

function solution1(n, k) {
  const answer = []
  for (let i = 0; k * i <= n; i++) {
    answer.push(k * i)
  }
  return answer
}

console.log(solution(10, 3))*5033