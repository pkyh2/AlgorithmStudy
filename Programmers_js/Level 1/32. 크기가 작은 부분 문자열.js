function solution(t, p) {
  var answer = 0;
  const len = t.length - p.length
  for (let i = 0; i < len + 1; i++) {
    if (parseInt(t.slice(i, p.length+i)) - parseInt(p) <= 0) {
      answer += 1
    }
  }
  return answer;
}

// 1. t에서 p길이만큼 문자열을 추출 한다.
// 2. t, p를 숫자로 변경하고 비교한다.
// 3. t <= p 면 cnt를 올린다.

console.log(solution("3141592", "271"))
console.log(solution("500220839878", "7"))
console.log(solution("10203", "15"))