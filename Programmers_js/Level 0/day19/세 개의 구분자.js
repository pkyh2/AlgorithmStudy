function solution(myStr) {
  let answer = myStr.split(/[abc]/).filter((v, _) => v);
  return answer.length === 0 ? ["EMPTY"] : answer;
}

console.log(solution("baconlettucetomato"));
console.log(solution("abcd"));
console.log(solution("cabab"));
