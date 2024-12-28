function solution(myString) {
  return myString
    .split("x")
    .filter((v, _) => v)
    .sort();
}

console.log(solution("axbxcxdx"));
console.log(solution("dxccxbbbxaaaa"));
