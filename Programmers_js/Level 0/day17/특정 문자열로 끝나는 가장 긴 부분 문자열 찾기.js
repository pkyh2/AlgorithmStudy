function solution(myString, pat) {
  const l1 = myString.length;
  const l2 = pat.length;
  for (let i = l1; i >= 0; i--) {
    const temp = myString.slice(i - l2, i);
    if (temp === pat) {
      return myString.slice(0, i);
    }
  }
}

// 맨 뒤에서 부터 pat 길이 씩 slice하여 pat랑 비교한다.
//

console.log(solution("AbCdEFG", "dE"));
