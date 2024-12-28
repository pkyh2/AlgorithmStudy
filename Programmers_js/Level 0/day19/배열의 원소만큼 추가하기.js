function solution(arr) {
  var answer = [];
  arr.forEach((v, i) => {
    answer.push(...Array.from({ length: v }, () => v));
  });
  return answer;
}

console.log(solution([5, 1, 4]));
console.log(solution([6, 6]));
console.log(solution([1]));
