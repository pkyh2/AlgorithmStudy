function solution(k, score) {
  var answer = [];
  let topScore = []

  for (const v of score) {
    if (topScore.length < k) {
      topScore.push(v)
      topScore.sort((a, b) => b - a)

      answer.push(topScore[topScore.length - 1])

    } else {
      topScore.push(v)
      topScore.sort((a, b) => b - a)
      topScore.pop()

      answer.push(topScore[topScore.length - 1])
    }
  }


  return answer;
}

// 1. topScore 배열의 길이가 k보다 길면 마지막 원소를 버린다.
// 2. 매번 topScore배열의 마지막 원소를 answer 배열에 push한다.
// 3. score 배열을 반복하면서 각 원소를 topScore에 push한다.
// 4. topScore 배열을 정렬한다.


console.log(solution(3, [10, 100, 20, 150, 1, 100, 200]))
console.log(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))