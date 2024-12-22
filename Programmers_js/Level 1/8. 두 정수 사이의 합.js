function solution(a, b) {
  var answer = 0;
  let smallNum = a > b ? b : a
  let bigNum = a > b ? a : b
  for (let i = smallNum; i <= bigNum; i++) {
    answer += i
  }
  return answer;
}


console.log(solution(5, 3))