function solution(a, b) {
    var answer = a.map((v, i) => v * b[i]).reduce((acc, cur) => acc + cur);
    return answer;
}

// 길이가 같은 두 배열의 내적
// 각 배열의 같은 idx의 곱의 합
console.log(solution([1,2,3,4], [-3,-1,0,2]))
console.log(solution([-1,0,1], [1,0,-1]))