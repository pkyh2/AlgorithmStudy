function solution(s) {
    if (s.length % 2 === 0) {
        return s.slice(s.length/2 - 1, s.length/2 + 1)
    } else {
        return s.slice(s.length/2, s.length/2 + 1)
    }
}

console.log(solution("abcde"))
console.log(solution("qwer"))