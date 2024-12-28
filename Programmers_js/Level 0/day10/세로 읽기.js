function solution2(my_string, m, c) {
  var answer = "";
  let strPart = "";
  const splitMyStr = [...my_string].map((char, i) => {
    strPart += char;
    if (i + (1 % m) === 0) {
      return strPart;
    }
  });
  console.log("🚀 ~ splitMyStr ~ splitMyStr:", splitMyStr);
  return answer;
}

function solution(my_string, m, c) {
  let answer = "";
  let i = 0;
  while (i < Math.floor(my_string.length / m)) {
    const splitMyStr = my_string.slice(i * m, (i + 1) * m).split("");
    answer += splitMyStr[c - 1];
    i++;
  }
  return answer;
}

console.log(solution("ihrhbakrfpndopljhygc", 4, 2));

// m번 반복해서 my_string을 분리
