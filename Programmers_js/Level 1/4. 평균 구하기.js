function solution(arr) {
  return arr.reduce((acc, cur) => acc + cur) / arr.length
}

console.log(solution([1,2,3,4]))