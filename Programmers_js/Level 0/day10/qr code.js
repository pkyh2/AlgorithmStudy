function solution(q, r, code) {
  return [...code].filter((_, i) => i % q === r).join("");
}

console.log(solution(3, 1, "qjnwezgrpirldywt"));
