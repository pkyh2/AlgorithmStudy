function solution(my_string, queries) {
  var answer = my_string;

  for (query of queries) {
    const parts = [...answer]
      .slice(query[0], query[1] + 1)
      .reverse()
      .join("");

    answer = answer.slice(0, query[0]) + parts + answer.slice(query[1] + 1);
  }
  return answer;
}

console.log(
  solution("rermgorpsam", [
    [2, 3],
    [0, 7],
    [5, 9],
    [6, 10],
  ])
);
