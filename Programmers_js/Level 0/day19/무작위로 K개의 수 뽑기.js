function solution(arr, k) {
  var answer = [];
  arr.forEach((v, i) => {
    if (answer.length !== k && !answer.includes(v)) {
      answer.push(v);
    }
  });
  if (answer.length < k) {
    // answer 배열의 가장 끝 원소에서, 삭제가 아니고 추가(0) 하고, k에서 answer 길이만큼 뺀 수 만큼 -1을 생성하여 추가한다.
    answer.splice(answer.length, 0, ...Array(k - answer.length).fill(-1));
  }
  return answer;
}

console.log(solution([0, 1, 1, 2, 2, 3], 3));
console.log(solution([0, 1, 1, 1, 1], 4));
