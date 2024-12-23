const solution = (price, money, count) => {
    let total_price = 0
    for (let i = 0; i < count; i++) {
        total_price += price * (i+1)
    }

    return total_price - money > 0 ? total_price - money : 0
}

// 1. 1회 이용료를 n번 탄 총 금액을 구한다.
// 2. Money에서 그 금액을 뺀다.

// 3. count 만큼 반복하여 idx + 1을 price와 곱하여 이용료를 구한다.
console.log(solution(3, 20, 4))