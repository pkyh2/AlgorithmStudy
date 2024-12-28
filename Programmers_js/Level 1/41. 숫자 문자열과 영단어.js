function solution(s) {
  var answer = s;
  const numbersStr = 
    {
      "zero": 0,
      "one": 1,
      "two": 2,
      "three": 3,
      "four": 4,
      "five": 5,
      "six": 6,
      "seven": 7,
      "eight": 8,
      "nine": 9
    }
  
  for (const [k, v] of Object.entries(numbersStr)) {
    if (s.includes(k)) {
      answer = answer.replaceAll(k, v)
    }
  }
  return Number(answer)
}

console.log(solution("oneone4seveneight"))
console.log(solution("23four5six7"))
console.log(solution("2three45sixseven"))
console.log(solution("123"))
console.log(solution("1zerotwozero3"))

