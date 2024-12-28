function solution(myString) {
  return [...myString].map((v, i)=> v < 'l' ? 'l' : v).join('')
}

// 알파벳 L 보다 앞서는 모든 문자를 l로 변경
console.log(solution("abcdevwxyz"))
console.log(solution("jjnnllkkmm"))