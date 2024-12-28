function solution(num_list) {
  const sum = num_list.reduce((acc, cur) => acc + cur);
  const mult = num_list.reduce((acc, cur) => acc * cur);
  if (sum**2 > mult) {
    return 1;
  } else {
    return 0
  }
}


// 모든 원소들의 곱이 / 합의 제곱 보다 작으면 1


console.log(solution([1, 2, 3])) // 1