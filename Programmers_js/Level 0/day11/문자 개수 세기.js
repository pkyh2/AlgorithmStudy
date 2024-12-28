function solution(my_string) {
  var answer = [...Array(52)].map(() => 0);
  const upperAlphabet = [...Array(26)].map((_, i) =>
    String.fromCharCode(i + 65)
  );
  const lowerAlphabet = [...Array(26)].map((_, i) =>
    String.fromCharCode(i + 97)
  );
  const allAlphabet = [...upperAlphabet, ...lowerAlphabet];
  [...my_string].map((char, i) => {
    return (answer[allAlphabet.findIndex((ele) => ele === char)] += 1);
  });

  return answer;
}

console.log(solution("Programmers"));
