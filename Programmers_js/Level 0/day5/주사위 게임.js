function solution(a, b, c) {
  var answer = 0;
  if (a === b && b === c) {
    answer = (a+b+c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3);
  } else if (a === b || b === c || a === c) {
    answer = (a+b+c) * (a**2 + b**2 + c**2);
  } else {
    answer = a + b + c;
  }
  return answer;
}

// 3 숫자가 모두 다르면 a + b + c
// 2 숫자가 가

console.log(solution(1, 2, 3)) // 6
console.log(solution(5, 3, 3)) // 6
console.log(solution(4, 4, 4)) // 6