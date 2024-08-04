function solution(n) {
  var answer = [n];
  while (n !== 1) {
    n = n % 2 === 0 ? n / 2 : 3 * n + 1;
    answer.push(n);
  }
  return answer;
}

// n이 짝수이면 2로 나누고, n이 홀수이면, 3*n+1을 한다.
console.log(solution(10)); // [0, 1, 2, 3, 4]
