function solution(x1, x2, x3, x4) {
  var answer = (x1 || x2) && (x3 || x4);
  return answer;
}

console.log(solution(true, false, false, false));
