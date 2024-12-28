function solution(num_list) {
  const sumEven = num_list.reduce((acc, cur, idx) => {
    // 홀수 일 때
    if (idx % 2 === 0) {
      return acc + cur;
    }
    return acc;
  }, 0);
  const sumOdd = num_list.reduce((acc, cur, idx) => {
    if (idx % 2 !== 0) {
      return acc + cur;
    }
    return acc;
  }, 0);
  return sumEven > sumOdd ? sumEven : sumOdd;
}

console.log(solution([4, 2, 6, 1, 7, 6]));
