function solution(ineq, eq, n, m) {
  if (eq === "=") {
    if (ineq === ">") {
      if (n >= m) return 1
      else return 0
    } else if (ineq === "<") {
      if (n <= m) return 1
      else return 0
    }
  } else {
    if (ineq === ">") {
      if (n > m) return 1
      else return 0
    } else if (ineq === "<") {
      if (n < m) return 1
      else return 0
    }
  }
}

console.log(solution("<", "=", 20, 50))
console.log(solution(">", "!", 41, 78))