function solution(arr, idx) {
  let answer = [];
  arr.forEach((num, i) => {
    if (i >= idx && num === 1) {
      answer.push(i);
    }
  });
  return answer.length > 0 ? Math.min(...answer) : -1;
}

console.log(solution([0, 0, 0, 1], 1));
console.log(solution([1, 0, 0, 1, 0, 0], 4));
console.log(solution([1, 1, 1, 1, 0], 3));
// idx보다는 크면서 배열의 값이 1인 가장 작은 인덱스
