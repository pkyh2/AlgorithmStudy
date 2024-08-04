function solution(start_num, end_num) {
  var answer = Array.from({length: end_num-start_num+1}, (v, i) => start_num + i);
  return answer;
}

console.log(solution(3, 10)) // [10, 9, 8, 7, 6, 5, 4]