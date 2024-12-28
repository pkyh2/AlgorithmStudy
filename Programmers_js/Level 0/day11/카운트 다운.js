function solution(start, end_num) {
  var answer = Array.from({length: start - end_num + 1}, (_, i) => start - i)
  return answer;
}

console.log(solution(10, 3))