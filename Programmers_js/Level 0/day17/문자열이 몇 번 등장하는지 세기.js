function solution(myString, pat) {
  let cnt = 0;
  const leng = myString.length - pat.length + 1;
  for (let i = 0; i < leng; i++) {
    const temp = myString.slice(i, pat.length + i);
    if (temp === pat) {
      cnt++;
    }
  }

  return cnt;
}

console.log(solution("banana", "ana"));
console.log(solution("aaaa", "aa"));
