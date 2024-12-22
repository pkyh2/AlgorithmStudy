function solution(num) {
  if (num === 1 ) return 0
  var answer = num
  let i = 500
  let cnt = 0

  while (i > 0) {
    if (answer % 2 === 0) {
      answer /= 2
    } else {
      answer *= 3
      answer += 1
    }
    cnt++;
    i--;

    if (answer === 1) return cnt

  }
  return -1;
}

/*
1. 입력된 수가 짝수면 2로 나눈다.
2. 입력된 수가 홀수면 3을 곱하고 1을 더한다.
3. 결과가 1이 될 때 까지 반복한다.
4. 500번 반복할 때까지 1이 되지 않으면 -1을 반환한다.
*/

console.log(solution(1))
console.log(solution(6))
console.log(solution(16))
// console.log(solution(626331))