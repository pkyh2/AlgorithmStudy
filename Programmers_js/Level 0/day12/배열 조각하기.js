function solution(arr, query) {
  var answer = arr;
  query.forEach((q, i) => {
    if (i % 2 === 0) {
      answer = answer.slice(0, q + 1);
    } else {
      answer = answer.slice(q);
    }
  });
  return answer;
}

console.log(solution([0, 1, 2, 3, 4, 5], [4, 1, 2]));
