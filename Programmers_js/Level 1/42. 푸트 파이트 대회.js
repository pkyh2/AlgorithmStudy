function solution(food) {
  var answer = '';

  for (let i = 1; i < food.length; i++) {
    if (food[i] > 1) {
      const halfValue = Math.floor(food[i]/2)
      for (let j = 0; j < halfValue; j++) {
        answer += i
      }
    }
  }

  return answer + '0' + [...answer].reverse().join('');
}


// 1. food를 반복하면서 idx 1부터 끝까지 반복한다.
// 2. 원소의 절반 만큼 idx 값을 저장한다.
// 3. 생성된  문자열 값을 mirror 한다.

console.log(solution([1, 3, 4, 6]))
console.log(solution([1, 7, 1, 2]))