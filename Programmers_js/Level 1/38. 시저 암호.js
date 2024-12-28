const solution = (s, n) => {
  let result = '';

  for (let i = 0; i < s.length; i++) {
    let toASCII = s.charCodeAt(i)
    // 대문자 일때
    if (toASCII >= 65 && toASCII <= 90) {
      toASCII += n
      if (toASCII > 90) {
        toASCII -= 26
      }
      result += String.fromCharCode(toASCII)
    } else if (toASCII >= 97 && toASCII <= 122) { // 소문자 일때
      toASCII += n
      if (toASCII > 122) {
        toASCII -= 26
      }
      result += String.fromCharCode(toASCII)
    } else if (toASCII === 32) {
      result += String.fromCharCode(toASCII)
    };
  }
  return result
}

console.log(solution("AB", 1))
console.log(solution("a B z", 4))
console.log(solution("z", 1))
console.log(solution("abcdefghijklmnopqrstuvwxyz", 1))
console.log(solution("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 17))