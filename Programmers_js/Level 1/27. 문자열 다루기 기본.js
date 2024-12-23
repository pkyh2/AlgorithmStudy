const solution = (s) => {
    if (s.length === 4 || s.length === 6) {
        const isAlphabet = [...s].filter(v => isNaN(v))
    
        return isAlphabet.length === 0 ? true : false;
    } else {
        return false;
    }
}

console.log(solution("a234"))
console.log(solution("1234"))
console.log(solution("0a1234X"))