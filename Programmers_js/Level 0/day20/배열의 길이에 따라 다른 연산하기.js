function solution(arr, n) {
  var answer = [];
  if (arr.length % 2 === 0) {
    answer = arr.map((v, i) => (i % 2 === 0 ? v : v + n));
  } else {
    answer = arr.map((v, i) => (i % 2 === 0 ? v + n : v));
  }
  return answer;
}

// 배열 길이가 홀수면, 짝수 인덱스에 n을 더하고
// 배열의 길이가 짝수면, 홀수 인덱스에 n을 더한다.
console.log(solution([49, 12, 100, 276, 33], 27));
