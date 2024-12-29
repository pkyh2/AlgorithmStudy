function solution(name, yearning, photo) {
  var answer = [];
  const photoScore = name.map((v, i) => [v, yearning[i]])

  for (const v of photo) {
    let score = 0
    v.forEach((value, idx) => {
      if(name.includes(value)) {
        score += photoScore[name.indexOf(value)][1]
      }
    })
    answer.push(score)
  }
  return answer;
}

// 1. name과 yearning를 객체로 만든다.

console.log(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
console.log(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))