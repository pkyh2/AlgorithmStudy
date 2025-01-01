function solution(k, m, score) {
  var answer = 0;
  const sortScore = score.sort((a, b) => b - a)
  const len = parseInt(sortScore.length / m)

  for (let i = 0; i < len; i++) {
    let box = sortScore.slice(i*m, i*m + m)
    const minScore = Math.min(...box)
    if (minScore <= k) {
      answer += minScore * m
    }
  }

  return answer;
}

// 1. 포장개수는 m으로 나눠서 한다.
// 2. 최대한 높은 점수로 상자를 먼저 만들어야 된다.(내림 차순 정렬)
// 3. 상자를 만들어 점수를 계산한다.


console.log(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
console.log(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))