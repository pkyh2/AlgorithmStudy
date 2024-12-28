const solution = (arr) => {
  let stack = []
  for (const v of arr) {
   stack.push(v)
   if (stack.length > 1) {
    if (stack[stack.length - 2] === stack[stack.length - 1]) {
      stack.pop()
    }
   } 
  }
  return stack;
}

// 1. stack 배열을 생성한다.
// 2. arr을 반복한다.
// 3. stack 배열에 arr원소를 넣는다.
// 4. arr에서 넣는 원소가 stack의 가장 마지막 원소와 같으면 넣지 않는다.


console.log(solution([1,1,3,3,0,1,1]))
console.log(solution([4,4,4,3,3]))