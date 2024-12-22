function solution(arr, delete_list) {
  var answer = [];
  arr.forEach((v, i) => {
    if (!delete_list.includes(v)) {
      answer.push(v);
    }
  });
  return answer;
}

console.log(solution([293, 1000, 395, 678, 94], [94, 777, 104, 1000, 1, 12]));
