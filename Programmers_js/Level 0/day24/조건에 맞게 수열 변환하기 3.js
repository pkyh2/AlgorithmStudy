function solution(arr, k) {
  return k % 2 === 0 ? arr.map((v, i) => v + k) : arr.map((v, i) => v * k)
}

console.log(solution([1, 2, 3, 100, 99, 98], 3))
console.log(solution([1, 2, 3, 100, 99, 98], 2))