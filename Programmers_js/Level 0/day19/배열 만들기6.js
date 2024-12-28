function solution(arr) {
  var answer = [];
  arr.forEach((v, i) => {
    if (answer.at(-1) === v) {
      answer.pop();
    } else {
      answer.push(v);
    }
  });
  return answer.length === 0 ? [-1] : answer;
}

console.log(solution([0, 1, 1, 1, 0]));
