const solution = (s) => {
  let changedWord = []
  for (const v of s.split(' ')) {
    changedWord.push([...v].map((v, i) => i % 2 === 0 ? v.toUpperCase() : v.toLowerCase()).join(''))
  }
  return changedWord.join(' ');
}


// 1. 짝수번째 알파벳은 대문자
// 2. 홀수번째 알파벳은 소문자
console.log(solution("try hello world"))