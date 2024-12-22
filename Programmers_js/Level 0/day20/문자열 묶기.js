function solution(strArr) {
  var answer = 0;
  const cntArr = [];
  strArr.forEach((v, i) => {
    cntArr.push(v.length.toString());
  });

  const count = cntArr.reduce((acc, cur) => {
    acc[cur] = (acc[cur] || 0) + 1;
    return acc;
  }, {});

  answer = Math.max(...Object.values(count));
  return answer;
}

console.log(solution(["a", "bc", "d", "efg", "hi"]));
