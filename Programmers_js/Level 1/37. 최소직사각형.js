const solution = (sizes) => {
  let bigArr = []
  let smallArr = []
  for (const arr of sizes) {
    if (arr[0] > arr[1]) {
      bigArr.push(arr[0])
      smallArr.push(arr[1])
    } else {
      bigArr.push(arr[1])
      smallArr.push(arr[0])
    }
  }
  return Math.max(...bigArr) * Math.max(...smallArr)
}

console.log(solution([
  [60, 50], 
  [30, 70], 
  [60, 30], 
  [80, 40]
]))

console.log(solution([
  [10, 7], 
  [12, 3], 
  [8, 15], 
  [14, 7], 
  [5, 15]
]))

// 가장 큰수
// 큰수 끼리 작은수 끼리
// 10, 12, 15, 14, 15
// 7, 3, 8, 7, 5, 