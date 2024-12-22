function solution(arr, queries) {
  var answer = arr;
  for (q of queries) {
    for (let i = q[0]; i <= q[q.length - 1]; i++) {
      answer[i] += 1;
    }
  }
  return answer;
}

console.log(
  solution(
    [0, 1, 2, 3, 4],
    [
      [0, 1],
      [1, 2],
      [2, 3],
    ]
  )
);
