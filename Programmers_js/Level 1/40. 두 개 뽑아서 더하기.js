function solution(numbers) {
  var answer = [];
  const len = numbers.length
  for (let i = 0; i < len; i++) {
    for (let j = i+1; j < len; j++) {
      console.log("plus:", numbers[i], numbers[j])
      answer.push(numbers[i] + numbers[j])
    }
  }
  const result = new Set(answer)
  return [...result].sort((a, b) => a - b);
}


// numbers에서 서로 다른 두 개의 수를 뽑는다.
// 1, 2나 2, 1은 같은것이다.
// 조합으로 뽑는다.

console.log(solution([2,1,3,4,1]))
console.log(solution([5,0,2,7]))