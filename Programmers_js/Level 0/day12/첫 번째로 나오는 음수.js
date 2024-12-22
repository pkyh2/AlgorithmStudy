function solution(num_list) {
  // reduce메서드에서 콜백 함수가 반환한 값을 누적기에 저장한다.
  const answer = num_list.reduce((acc, num, idx) => {
    console.log("acc", acc)
    if (acc !== -1) return acc;
    console.log("debug1")
    if (num < 0) return idx;
    return acc
  }, -1)
  return answer

  // const answer = num_list.filter(a => {if (a < 0) return a})
  // return num_list.indexOf(answer[0])
}

console.log(solution([12, 4, 15, 46, 38, -2, 15]))
console.log(solution([13, 22, 53, 24, 15, 6]))