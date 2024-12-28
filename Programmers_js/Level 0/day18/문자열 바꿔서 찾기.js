function solution(myString, pat) {
  return [...myString]
    .map((v, i) => (v === "A" ? "B" : "A"))
    .join("")
    .includes(pat)
    ? 1
    : 0;
}

console.log(solution("ABBAA", "AABB"));
