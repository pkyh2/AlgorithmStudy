function solution(phone_number) {
  const frontNum = [...phone_number.slice(0, -4)].map(v => "*").join('');
  const backNum = phone_number.slice(-4)
  
  return frontNum + backNum;
}

console.log(solution("01033334444"))
console.log(solution("027778888"))