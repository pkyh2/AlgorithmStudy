function solution(arr, queries) {
  var answer = arr;
  for(query of queries) {
    const [start, end] = query;
    let temp = arr[start]
    answer[start] = arr[end]
    answer[end] = temp
  }
  return answer;
}

// function solution(arr, queries) {
//     for(let [i, j] of queries) {
//         [arr[i], arr[j]] = [arr[j], arr[i]];
//     }
//     return arr;
// }
console.log(solution([1, 2, 3, 4, 5], [[1, 2], [1, 3], [2, 4]])) // [2, 3, 3]
console.log(solution([0, 1, 2, 3, 4], [[0, 3],[1, 2],[1, 4]])) // [2, 3, 3]