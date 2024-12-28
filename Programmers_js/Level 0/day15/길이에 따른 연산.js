function solution(num_list) {
  var answer = 0;
  if (num_list.length > 10) {
    answer = num_list.reduce((arr, cur) => arr + cur);
  } else {
    answer = num_list.reduce((arr, cur) => arr * cur);
  }
  return answer;
}

// 중괄호가 없으면 표현식의 결과(return)다.
// 중괄호가 있으면 return 키워드로 명시적으로 값을 반환해야 된다.
const solution = (list) =>
  list.reduce((a, c) => (list.length > 10 ? a + c : a * c));

console.log(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]));
console.log(solution([2, 3, 4, 5]));
