function solution(arr) {
  var answer = arr;
  // arr의 길이가 2의 제곱수보다 작은지 확인
  for (let i = 0; i < 11; i++) {
    const PowerOfTwo = 2 ** i;
    if (arr.length === PowerOfTwo) {
      return answer;
    } else if (arr.length < PowerOfTwo) {
      answer.push(...Array(PowerOfTwo - arr.length).fill(0));
      break;
    }
  }
  return answer;
}

console.log(solution([1, 2, 3, 4, 5, 6]));
console.log(solution([58, 172, 746, 89]));
