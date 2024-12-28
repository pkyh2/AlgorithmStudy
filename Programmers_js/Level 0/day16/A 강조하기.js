function solution(myString) {
  return [...myString]
    .map((char, i) => (char === "a" || char === "A" ? "A" : char.toLowerCase()))
    .join("");
}

console.log(solution("abstract algebraAA"));
console.log(solution("PrOgRaMmErS"));
