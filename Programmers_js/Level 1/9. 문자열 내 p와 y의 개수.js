function solution(s){
  const arr = [...s.toLowerCase()]
  let pCnt = 0
  let yCnt = 0

  arr.forEach((v, i) => {
    if (v === 'p') pCnt += 1
    else if (v === 'y') yCnt += 1
  })

  return pCnt === yCnt;
}

console.log(solution("pPoooyY"))
console.log(solution("Pyy"))