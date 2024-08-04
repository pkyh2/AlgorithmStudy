function solution(my_string, n) {
  var answer = my_string.slice(-n);
  return answer;
}

console.log(solution("ProgrammerS123", 11)) // def
console.log(solution("He110W0r1d", 5)) // def