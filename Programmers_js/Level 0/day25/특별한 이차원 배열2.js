function solution(arr) {
  var answer = 1;
  for (let i = 0; i < arr.length; i++){
    for (let j = 0; j < arr.length; j++) {
      if (arr[i][j] !== arr[j][i]) {
        return 0
      }
    }
  }
  return answer;
}

function solution2(arr) {
  return arr.every((v, i) => v.every((_, j) => arr[i][j] === arr[j][i])) ? 1: 0
}

console.log(solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]]))
console.log(solution([[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]))
console.log(solution2([[5, 192, 33], [192, 72, 95], [33, 95, 999]]))
console.log(solution2([[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]))
