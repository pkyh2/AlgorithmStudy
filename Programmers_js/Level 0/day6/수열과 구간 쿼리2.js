// function solution(arr, queries) {
//   var answer = [];
//   for(query of queries) {
//     const [start, end, flag] = query;
//     const resultNum = arr.slice(start, end+1).filter((v, i) => flag < v)
//     if (resultNum.length === 0) {
//       answer.push(-1)
//     } else {
//       answer.push(Math.min(...resultNum))
//     }
//   }
//   return answer;
// }

function solution(arr, queries) {
  return queries.map(
    ([s, e, k]) =>
      arr
        .slice(s, e + 1)
        .filter((n) => n > k)
        .sort((a, b) => a - b)[0] || -1
  );
}

// console.log(solution([1, 2, 3, 4, 5], [[1, 2], [1, 3], [2, 4]])) // [2, 3, 3]
console.log(
  solution(
    [0, 1, 2, 4, 3],
    [
      [0, 4, 2],
      [0, 3, 2],
      [0, 2, 2],
    ]
  )
); // [2, 3, 3]
