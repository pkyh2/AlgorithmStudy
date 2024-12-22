function solution(picture, k) {
  var answer = [];
  for (v1 of picture) {
    let oneLine = ""
    
    v1.split("").forEach((v, i) => {
      if (v === ".") {
        for (let j = 0; j < k; j++) {
          oneLine += "."
        }
      } else if (v === "x") {
        for (let j = 0; j < k; j++) {
          oneLine += "x"
        }
      }
    })

    for (let i = 0; i < k; i++) {
      answer.push(oneLine)
    } 
  }
  return answer;
}


console.log(solution([
  ".xx...xx.",
  "x..x.x..x",
  "x...x...x",
  ".x.....x.",
  "..x...x..",
  "...x.x...",
  "....x...."], 
  2)
)
  
console.log(solution([
  "x.x",
  ".x.",
  "x.x"],
  3)
)



/*
1. 첫 원소 개수의 k배 변경되면 2배
*/