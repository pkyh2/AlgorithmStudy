function solution(str_list, ex) {
  var answer = '';
  for (str of str_list) {
    if (!str.includes(ex)) {
      answer += str;
    }
  }
  return answer;
}


console.log(solution(["abc", "def", "ghi"], "ef")) // apple
console.log(solution(["abc", "bbc", "cbc"], "c")) // apple