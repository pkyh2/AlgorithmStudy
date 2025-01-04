// 최악
// function solution(n) {
//   const temp = []
//   for (let i = 2; i <= n; i++) { // 2부터 10까지 반복
//     // 2가 소수인지 확인
//     let cnt = 0
//     for (let j = 1; j*j <= i; j++) {
//       if (i % j === 0) {
//         cnt += 1
//       }
//     }
//     if (cnt === 2) {
//       temp.push(i)
//     }
    
//   }
//   return temp.length;
// }

// 어떤 소수도 N의 제곱근보다 큰 수로 나눠지지 않는다.
// 17이 소수인지 확인해보려면 17의 제곱근 까지 반복했을 때 17이 나눠지는지 확인해보면 된다.
const solution = (n) => {
  const answer = []
  for (let i = 2; i <= n; i++) {
    answer.push(isPrime(i))
  }
  return answer.filter(v => v !== false).length
}

const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return num;
}



// 에라토스테네스의 체
// 1. 2부터 n까지 수가 있는 배열을 만든다.
// 2. 2, 3은 소수가 아니니 false처리 한다.
// 3. 배열을 반복한다.
// 4. 원소가 true면 그 원소의 배수를 모두 지운다.

// 2, 3, 5의 배수를 지워 나가고 남은 수가 소수이다.
const solution1 = (n) => {
  let arr = Array.from({length: n + 1}).fill(true).fill(false, 0, 2)
  const sqrt = parseInt(Math.sqrt(n))

  for (let i = 2; i <= sqrt; i++) {
    if (arr[i] === true) {
      for (let j = 2; i * j <= n; j++) {
        arr[i * j] = false
      }
    }  
  }
  return arr.filter(v => v === true).length
}

// 소수는 1과 자기 자신
// console.log(solution(10)) 
console.log(solution1(10)) 