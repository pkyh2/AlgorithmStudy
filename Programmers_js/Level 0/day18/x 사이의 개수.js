function solution(myString) {
  return myString.split("x").map((v, _) => v.length);
}

console.log(solution("oxooxoxxox"));
console.log(solution("xabcxdefxghi"));
