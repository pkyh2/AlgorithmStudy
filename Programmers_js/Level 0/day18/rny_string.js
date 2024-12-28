function solution(rny_string) {
  return [...rny_string].map((v, i) => (v === "m" ? "rn" : v)).join("");
}

console.log(solution("masterpiece"));
