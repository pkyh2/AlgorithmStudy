const solution = (left, right) => {
    let numSum = 0
    const numArr = Array.from({length: right - left + 1}, (_, i) => i + left)
    numArr.map((v, i) => {
        const divisors = []
        for (let i = 1; i <= v; i++) {
            if (v % i === 0) {
                divisors.push(i)
            }
        }

        if (divisors.length % 2 === 0) {
            numSum += v
        } else {
            numSum -= v
        }
    })

    return numSum;
}

// 꿀팁 제곱근이 정수면 약수의 개수가 홀수다.

// left에서 right까지 각 수의 약수의 개수가 짝수면 더하고 홀수면 빼라
// 1. left, right까지 배열을 생성
// 2. 배열을 반복하면 약수 개수를 구한다.
// 3. 약수 개수가 짝수개 인지 홀수개 인지 확인
// 4. 짝수개면 더하고 홀수개면 뺀다.
console.log(solution(13, 17)); // 43