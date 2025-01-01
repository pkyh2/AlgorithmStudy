function solution(a, b) {
  const divisor_day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
  const days_31 = [1, 3, 5, 7, 8, 10, 12]
  const days_30 = [4, 6, 9, 11]
  const days_29 = 2

  let total_days = 0

  for (let i = 1; i < a; i++) {
    if (days_31.includes(i)) {
      total_days += 31
    } else if (days_30.includes(i)) {
      total_days += 30
    } else if (i === days_29) {
      total_days += 29
    }
  } 

  total_days += b
  const idx = total_days % 7 - 1 < 0 ? 6 : total_days % 7 - 1

  return divisor_day[idx];
}

console.log(solution(10, 24))
console.log(solution(5, 24))
console.log(solution(1, 1))
console.log(solution(12, 31))
console.log(solution(9, 1))