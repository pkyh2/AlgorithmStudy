function solution(numbers, n) {
  var answer = numbers[0];
  let i = 1;
  while (answer <= n) {
    answer += numbers[i];
    i++;
  }
  return answer;
}

console.log(solution([34, 5, 71, 29, 100, 34], 123));
console.log(solution([58, 44, 27, 10, 100], 139));
