function solution(n) {
  return [...n.toString()].map((v, _) => Number(v)).reverse()
}

console.log(solution(12345))