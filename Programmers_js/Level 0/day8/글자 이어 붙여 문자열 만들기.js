function solution(my_string, index_list) {
  var answer = '';
  for (num of index_list) {
    answer += my_string[num];
  }
  return answer;
}

console.log(solution("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7])) // Prgmr
console.log(solution("zpiaz", [1, 2, 0, 0, 3])) // Prgmr