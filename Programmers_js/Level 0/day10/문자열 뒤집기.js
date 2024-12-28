function solution(my_string, s, e) {
  var answer = my_string;
  const reversedStr = [...my_string.slice(s, e + 1)].reverse().join("");
  answer = answer.replace(my_string.slice(s, e + 1), reversedStr);
  return answer;
}

console.log(solution("Progra21Sremm3", 6, 12));
