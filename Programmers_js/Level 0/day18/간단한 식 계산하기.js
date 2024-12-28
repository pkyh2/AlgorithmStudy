function solution(binomial) {
  var answer = 0;
  if (binomial.includes("+")) {
    answer = binomial.split(" + ").reduce((acc, cur) => {
      return parseInt(acc) + parseInt(cur);
    });
  } else if (binomial.includes("-")) {
    answer = binomial.split(" - ").reduce((acc, cur) => {
      return parseInt(acc) - parseInt(cur);
    });
  } else if (binomial.includes("*")) {
    answer = binomial.split(" * ").reduce((acc, cur) => {
      return parseInt(acc) * parseInt(cur);
    });
  }
  return answer;
}

console.log(solution("43 + 12"));
console.log(solution("0 - 7777"));
console.log(solution("40000 * 40000"));
