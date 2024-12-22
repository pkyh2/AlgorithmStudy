function solution(num_str) {
  return [...num_str]
    .map((v, i) => parseInt(v))
    .reduce((acc, cur) => {
      return acc + cur;
    });
}

console.log(solution("123456789"));
