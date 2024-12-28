function solution(names) {
  var answer = [];
  names.filter((name, idx) => {
    if (idx % 5 === 0) {
      answer.push(names[idx]);
    }
  });
  return answer;
}

console.log(
  solution(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"])
);
