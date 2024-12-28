function solution(order) {
  var answer = 0;
  for (v of order) {
    if (v === "anything") {
      answer += 4500
    } else if (v.includes("americano")) {
      answer += 4500
    } else if (v.includes("cafelatte")) {
      answer += 5000
    }
  }
  return answer;
}


console.log(solution(["cafelatte", "americanoice", "hotcafelatte", "anything"]))
console.log(solution(["americanoice", "americano", "iceamericano"]))


/*
1. 메뉴만 적었으면 ice다.
2. "anything" 면 iceamericano다.


1. order를 반복한다.
2. anything이면 4,500원을 더한다.
3. americano가 있으면 4,500원을 더한다.
4. cafelatte면 5,000원을 더한다.
*/