function solution(a, b) {
  const sum = BigInt(a) + BigInt(b);
  return sum.toString();
}

console.log(solution("582", "734"));
console.log(solution("0", "0"));
console.log(solution("18446744073709551615", "287346502836570928366"));
