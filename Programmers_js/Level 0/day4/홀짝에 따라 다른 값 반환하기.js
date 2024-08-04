function solution(n) {
  var answer = 0;
  if (n % 2 === 0) {
    // n길이의 배열을 생성한 다음
    // map 메서드로 각 배열을 반복하면서 num값을 출력
    answer = Array.from({length : n}, (_, i) => i + 1).filter(num => num % 2 === 0).reduce((acc, num) => acc + (num * num), 0) // 0을 추가해 준 이유는
  } else {
    answer = Array.from({length : n}, (_, i) => i + 1).filter(num => num % 2 !==0).reduce((acc, num) => acc + num, 0)
  }
  return answer;
}

console.log(solution(7))
console.log(solution(10))
