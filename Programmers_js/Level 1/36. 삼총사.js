const solution = (number) => {
  let cnt = 0
  const len = number.length
  for (let i = 0; i < len; i++) {
    for (let j = i+1; j < len; j++) {
      for (let k = j+1; k < len; k++) {
        const triple = number[i] + number[j] + number[k]
        if (triple === 0) cnt++
        
      }
    }
  }
  return cnt
}

// 조합은 [A, B, C]나 [C, B, A]가 같은 것으로 본다.
console.log(solution([-2, 3, 0, 2, -5]))