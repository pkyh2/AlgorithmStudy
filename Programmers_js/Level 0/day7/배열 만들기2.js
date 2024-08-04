function solution(l, r) {
  var answer = Array.from({ length: r - l + 1 }, (v, i) => l + i).filter(
    (v, i) => {
      // every() 메서드는 배열 안의 모든 요소가 주어진 판별 함수를 통과하는지 테스트
      return [...v.toString()].every((v) => v === "0" || v === "5");
    }
  );
  return answer.length > 0 ? answer : [-1];
}

// 0과 5로만 이루어진 정수
console.log(solution(5, 555));
console.log(solution(10, 20));
