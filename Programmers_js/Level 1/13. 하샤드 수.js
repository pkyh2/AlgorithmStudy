function solution(x) {
  // const digitSum = [...x.toString()].map((v, _) => Number(v)).reduce((acc, cur) => acc + cur)
  const digitSum = [...x.toString()].reduce((acc, cur) => acc + Number(cur), 0)
  return x % digitSum === 0 ? true : false
}

/*
1. 수를 자리수로 나눈다.
2. 더한다
4. x와 나눠 떨어지는지 확인한다.
*/

console.log(solution(10))
console.log(solution(11))
console.log(solution(12))
console.log(solution(13))