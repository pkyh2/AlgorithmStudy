function solution(n, m) {
  let lcm = 0
  let gcd = 0

  for (let i = 1; i <= n; i++) {
    if (n % i === 0 && m % i === 0) {
      gcd = i
    }
  }

  lcm = n * m / gcd

  return [gcd, lcm];
}

// 1. 최소공배수(lcm)는 두 수의 가장 작은 배수가 될 수 있는수
// 12는 12의 1배수 3의 4배수
// 2. 최대 공약수(gcd)는 두 수의 가장 큰 공통된 약수

console.log(solution(3, 12))
console.log(solution(2, 5))