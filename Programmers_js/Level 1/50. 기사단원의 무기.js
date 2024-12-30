function solution(number, limit, power) {
  var answer = 0;
  const numbers = Array.from({length: number}, (_, i) => i+1)
  let divisorCnt = []

  for (const v of numbers) {
    const rootV = Math.sqrt(v)
    let cnt = 0
    for (let i = 1; i <= rootV; i++) {
      if (v % i === 0) {
        // 1 x 12, 12 x 1을 확인해서 2개인데
        // 4 x 4는 v === v / i라서 1개인거다.
        cnt += (i === v / i) ? 1 : 2; // 약수 1증가

      }
    }
    if (cnt > limit) divisorCnt.push(power)
    else divisorCnt.push(cnt)
  }

  answer = divisorCnt.reduce((acc, cur) => acc + cur)
  return answer;
}

// 1부터 number 까지 약수의 개수를 구한다.
// 각 개수가 limit을 넘는지 확인한다.
// limit보다 크면 power로 계산한다.

console.log(solution(5, 3, 2))
console.log(solution(10, 3, 2))