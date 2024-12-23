// const solution = (s) => {
//     return [...s].sort((a, b) => b.charCodeAt(0) - a.charCodeAt(0)).join('');
// }

const solution = (s) => {
    return [...s].sort().reverse().join('');
}
console.log(solution("Zbcdefg"))