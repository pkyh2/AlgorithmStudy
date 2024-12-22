function solution(n) {
  var answer = Array.from({length: n}, (v, i) => Array.from({length: n}, () => 0))
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (i === j) {
        answer[i][j] = 1;
      }
    }
  }
  return answer;
}

console.log(solution(3))