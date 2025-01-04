// function solution(nums) {
//   return combination(nums)
// }

// const combination = (arr) => {
//   const len = arr.length
//   let cnt = 0

//   for (let i = 0; i < len; i++) {
//     for (let j = i+1; j < len; j++) {
//       for (let k = j+1; k < len; k++) {
//         if(isPrime(arr[i] + arr[j] + arr[k])) cnt += 1
//       }
//     }
//   }
//   return cnt
// }

// const isPrime = (num) => {
//   const sqrt = parseInt(Math.sqrt(num))
//   if (num <= 1) return false
//   for (let i = 2; i <= sqrt; i++) {
//     if (num % i === 0) return false
//   }
//   return true
// }


const isPrime = (n) => {
  // 0 ~ n까지의 배열 생성 후 0, 1은 false 처리한다.
  let arr = Array.from({length: n + 1}).fill(true).fill(false, 0, 2)
  const sqrt = parseInt(Math.sqrt(n))

  // 2 index 부터 제곱근 수 까지의 배수를 제거
  for (let i = 2; i <= sqrt; i++) {
    if (arr[i] === true) {
      for (let j = 2; i * j <= n; j++) {
        // 원소와 idx가 같다.
        arr[i * j] = false
      }  
    }
  }
  return arr.reduce((acc, cur, idx) => {
    if (cur) acc.push(idx)
    return acc;
  }, [])
}
console.log(isPrime(10))

// 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 수를 구하시오
// 1. 주어진 숫자 중 3개를 뽑아 더할 수 있는 경우의 수를 모두 구하시오(순열)
// 2. 3개의 경우의 수가 담긴 배열에서 소수인 수의 개수를 구하시오.
// console.log(solution([1, 2, 3, 4]))
// console.log(solution([1, 2, 7, 6, 4]))