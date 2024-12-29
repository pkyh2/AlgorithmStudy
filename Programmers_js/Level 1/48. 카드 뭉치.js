function solution(cards1, cards2, goal) {
  const goalCandidate = goal.map((v, i) => {
    if (cards1[0] === v) {
      cards1.shift()
      return v
    } else if (cards2[0] === v) {
      cards2.shift()
      return v
    }
  })
  return JSON.stringify(goalCandidate) === JSON.stringify(goal) ? "Yes" : "No"
}

// cards2를 card1에 각각 넣어본다.
// 그냥 하나씩 빼서 goal이랑 같은지 확인해보면 된다.

console.log(solution(["i", "drink", "water"], 	["want", "to"], ["i", "want", "to", "drink", "water"]))
console.log(solution(["i", "water", "drink"], 	["want", "to"], ["i", "want", "to", "drink", "water"]))