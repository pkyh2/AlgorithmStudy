function solution(arr) {
  var answer = arr;
  let rowLen = arr[0].length
  let colLen = arr.length
  let lenDiff = Math.abs(arr.length - arr[0].length)
  
  for (let i = 0; i < lenDiff; i ++) {
    if (rowLen > colLen) {
      answer.push(Array.from({length: rowLen}, () => 0))
    } else {
      for (let j = 0; j < colLen; j++) {
        answer[j].push(0)
      }
    }
  }

  return answer;
}


console.log(solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]))
console.log(solution([[57, 192, 534, 2], [9, 345, 192, 999]]))
console.log(solution([[1, 2], [3, 4]]))