function solution(board, k) {
  var answer = 0;
  const rowLen = board[0].length
  const colLen = board.length
  for (let i = 0; i < colLen; i++) {
    for (let j = 0; j < rowLen; j++) {
      if (i + j <= k) {
        answer += board[i][j]
      }
    }
  }
  return answer;
}

console.log(solution([[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]], 2))
// i + j <= k