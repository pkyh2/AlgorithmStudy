const solution = (my_string, target) => {
  var a = my_string.includes(target);
  return a ? 1 : 0;

  let answer = 0;
  const length = my_string.length - target.length;
  for (let i = 0; i < length + 1; i++) {
    if (my_string.slice(i, length + i) === target) {
      answer = 1;
      return answer;
    }
  }
  return answer;
};

console.log(solution("banana", "ana"));
console.log(solution("banana", "wxyz"));

// 알고리즘 생각하기
// target 문자열을 my_string 길이에서 target 길이만큼 뺀 숫자만큼 반복문을 돈다.
// 이 때 target 문자열과 my_string 문자열에서 첫 인덱스부터 target 길이만큼의 index를 뽑아서
// 두 문자열을 비교한다.
// 일치하면 1을 내보내고 일치하지 않으면 다음 인덱스로 넘어간다.
// 반복문이 끝날 때 가지 문자열이 일치하지 않으면 0을 내보낸다.
