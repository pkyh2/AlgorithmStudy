function solution(n) {
  return [...String(n)].reduce((acc, cur) => acc + parseInt(cur), 0)
}

console.log(solution(123))