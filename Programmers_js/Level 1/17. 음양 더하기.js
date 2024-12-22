function solution(absolutes, signs) {
  let sum = 0
  return signs.reduce((acc, cur, i) => {
    if (cur) {
      sum += absolutes[i]
    } else {
      sum -= absolutes[i]
    }
    return sum
  }, 0)
}

console.log(solution([4,7,12], [true,false,true]))
console.log(solution([1,2,3], [false,false,true]))