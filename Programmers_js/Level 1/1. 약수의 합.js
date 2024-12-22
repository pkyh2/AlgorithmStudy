function solution(n) {
  let arr = Array.from({length: n}, (v, i) => i+1)
  let answer = arr.filter((v, i) => n % v === 0).reduce((acc, cur) => acc + cur, 0)
  return answer;
}

function solution2(n) {
  let answer = 0
  for (let i = 1; i <= n; i++) {
    if (n % i === 0) {
      answer += i
    }
  }
  return answer
}

// 10 => 1, 2, 5, 10

console.log(solution(10))
console.log(solution2(10))