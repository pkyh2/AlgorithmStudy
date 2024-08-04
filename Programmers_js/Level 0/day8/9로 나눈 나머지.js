function solution(number) {
  var answer =
    [...number].map((v) => parseInt(v)).reduce((acc, cur) => acc + cur, 0) % 9;
  return answer;
}

console.log(solution("123")); // 321
console.log(solution("78720646226947352489")); // 321
