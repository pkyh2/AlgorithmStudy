// function solution(n) {
//   return Number([...n.toString()].map((v, _) => Number(v)).sort((a, b) => b - a).join(''))
// }

function solution(n) {
  return Number([...n.toString()].map((v, _) => Number(v)).sort().reverse().join(''))
}
console.log(solution(118372))

/*
* compareFunction이 생략될 경우 , 배열의 요소들은 모두 문자열 취급되며, 유니코드 값 순서대로 정렬된다!

닫기
🍀 compareFunction : 정렬 순서를 정의하는 함수

이 함수는 두 개의 배열 요소를 파라미터로 입력 받음.
함수가 두 개의 배열 요소(a, b)로 입력 받을 경우
 a > b => return 1        // return value>0이므로 a는 b 뒤에 위치
a < b => return -1       // return value<0이므로 a는 b 앞에 위치
a = b => return 0        // a와 b의 순서 변함 없음
*/