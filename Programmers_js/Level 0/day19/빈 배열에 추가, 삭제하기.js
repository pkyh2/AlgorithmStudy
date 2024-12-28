function solution(arr, flag) {
  var answer = [];
  arr.forEach((v, i) => {
    if (flag[i]) {
      answer.push(...Array.from({ length: v * 2 }, () => v));
    } else {
      answer = answer.slice(0, -v);
    }
  });
  return answer;
}

console.log(solution([3, 2, 4, 1, 3], [true, false, true, false, false]));
