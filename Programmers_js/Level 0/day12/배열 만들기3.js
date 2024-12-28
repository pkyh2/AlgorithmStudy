// function solution(arr, intervals) {
//   var answer = [];
//   for (a of intervals) {
//     answer.push(...arr.slice(a[0], a[1] + 1));
//   }

//   return answer;
// }

function solution(arr, intervals) {
  const [[a, b], [c, d]] = intervals;
  return [...arr.slice(a, b + 1), ...arr.slice(c, d + 1)];
}
console.log(
  solution(
    [1, 2, 3, 4, 5],
    [
      [1, 3],
      [0, 4],
    ]
  )
);
