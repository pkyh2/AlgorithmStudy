// function solution(a, d, included) {
//   var answer = Array.from({length:included.length}, (_, i) => a + (d*i)).filter((_, i) => included[i] === true).reduce((acc, cur) => acc + cur, 0)
//   return answer;
// }


function solution(a, d, included) {
  // 이미 배열이 있으니까 included.reduce를 사용해서 풀어보자.
  return included.reduce((acc, include, i) => {
    if (include) {
      return acc + (a + (d * i));
    }
    return acc;
  }, 0);
}
console.log(solution(3, 4, [true, false, false, true, true]))