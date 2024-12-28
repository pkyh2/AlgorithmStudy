function solution(n) {
  var answer = Array.from({length: n}, () => Array.from({length: n}, () => 0))
  let num = 1;
  let row = 0;
  let col = 0;

  for (let i = n; i > 0; i -= 2) {
    // 오른쪽으로 이동
    for (let j = 0; j < i; j++) {
      answer[row][col] = num++;
      col++;
    }
    col--;
    row++;
    
    // 아래로 이동
    for (let j = 0; j < i - 1; j++) {
      answer[row][col] = num++;
      row++;
    }
    row--;
    col--;

    // 왼쪽으로 이동
    for (let j = 0; j < i - 1; j++) {
      answer[row][col] = num++;
      col--;
    }
    col++;
    row--;

    // 위로 이동
    for (let j = 0; j < i - 2; j++) {
      answer[row][col] = num++;
      row--;
    }
    row++;
    col++;

  }
  return answer;
}

console.log(solution(4))



