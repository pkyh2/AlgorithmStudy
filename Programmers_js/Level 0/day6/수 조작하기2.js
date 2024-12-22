function solution(numLog) {
  var answer = '';
  for (let i = 0; i < numLog.length - 1; i++) {
    const diff = numLog[i+1] - numLog[i];
    if (diff === 1) {
      answer += 'w'
    } else if (diff === -1) {
      answer += 's'
    } else if (diff === 10) {
      answer += 'd'
    } else if (diff === -10) {
      answer += 'a'
    }
  }
  return answer;
}

console.log(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1])) // 0