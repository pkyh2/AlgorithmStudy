function solution(str1, str2) {
  var answer = '';
  // str1에서 1글자 가져오고, str2에서 1글자 가져와서 더한다.
  for (let i = 0; i < str1.length; i++) {
    answer += str1[i]
    answer += str2[i]
  }
  console.log([...str1].map((x, idx) => x+str2[idx]))
  return answer;
}

console.log(solution("aaaaa", "bbbbb"))