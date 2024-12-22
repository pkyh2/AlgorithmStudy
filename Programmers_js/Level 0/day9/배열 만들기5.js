function solution(intStrs, k, s, l) {
  var answer = [];
  for (str of intStrs) {
    const intStr = parseInt(str.slice(s, s + l));
    if (intStr > k) {
      answer.push(intStr);
    }
  }
  return answer;
}

function solution2(intStrs, k, s, l) {
  const answer = intStrs
    .map((str) => +str.slice(s, s + l))
    .filter((str) => str > k);
  return answer;
}

console.log(
  solution2(["0123456789", "9876543210", "9999999999999"], 50000, 5, 5)
);
