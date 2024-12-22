function solution(arr) {
  let answer = [...arr] // 스프레드 연산자 또는 slice()를 사용하면 arr의 복사본이 저장된다.
  const minNum = arr.sort((a, b) => a - b).shift()
  answer = answer.filter(v => v !== minNum)

  return answer.length === 0 ? [-1] : answer
}

console.log(solution([4,3,2,1]))
console.log(solution([10]))