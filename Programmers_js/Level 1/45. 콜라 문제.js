// function solution(a, b, n) {
//   let coke = 0;
//   let bottleCnt = n
//   let divNum = 0

//   while (a < bottleCnt) {
//     // 빈병 나누기 a한 수의 b를 곱한 만큼 콜라를 준다.
//     coke = Math.floor(bottleCnt / a) * b

//     bottleCnt = bottleCnt + (bottleCnt % a)
//   }
//   return coke;
// }


function solution(a, b, n) {
  let answer = 0;
  while(n >= a) {
      // (빈병/a) * b개 만큼 콜라를 준다.
      const newBottles = Math.floor(n / a) * b;
      answer += newBottles;
      // 빈병은 콜라 개수에서 나머지 빈병을 더한다.
      n = newBottles + (n % a);
  }
  return answer;
}

console.log(solution(2, 1, 20))
console.log(solution(3, 1, 20))