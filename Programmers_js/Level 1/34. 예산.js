const solution = (d, budget) => {
  let bud = budget
  let cnt = 0
  d.sort((a, b) => a-b).forEach((v, i) => {
    if (v > bud) return cnt
    else {
      bud -= v
      cnt++;
    }
  })
  return cnt
}

// 1. d 를 순서대로 정렬
// 2. d를 반복하면서 bodget에서 각 원소를 뺴준다.
// 3. 동시에 cnt를 올린다.
// 4. bodget가 원소보다 작아질때 cnt를 return 한다.

console.log(solution([1,3,2,5,4, 10], 9))
console.log(solution([2, 2, 3, 3], 10))