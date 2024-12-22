const solution1 = (myString, pat) => {
  const l1 = myString.length;
  const l2 = pat.length;
  const leng = l1 - l2 + 1;

  if (l2 > l1) return 0;
  else {
    for (let i = 0; i < leng; i++) {
      const s = myString.slice(i, l2 + i).toUpperCase();
      const p = pat.toUpperCase();
      if (s === p) return 1;
      else return 0;
    }
  }
};

const solution2 = (myString, pat) => {
  const pattern = pat.toUpperCase();
  return myString.toUpperCase().includes(pattern) ? 1 : 0;
};

console.log(solution("AbCdEfG", "aBcdeg"));
console.log(solution("aaAA", "aaaaa"));
console.log(solution("aabbaa", "aaa"));
console.log(
  solution("abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
);
console.log(
  solution("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")
);
