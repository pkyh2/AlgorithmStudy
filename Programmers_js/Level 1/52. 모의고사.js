function solution(answers) {
    var answer = [];
    let checkAns = [];
    const supoja = {
        supoja1: [1, 2, 3, 4, 5],
        supoja2: [2, 1, 2, 3, 2, 4, 2, 5],
        supoja3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    const ans = { ans1: 0, ans2: 0, ans3: 0 };
    
    for (let i = 1; i <= Object.keys(supoja).length; i++) {
        
        let subSupoja = supoja[`supoja${i}`]
        let subAns = ans[`ans${i}`]

        // 답안지 작성
        // supoja.length < answers.length 길이 만큼 답 수정
        if (subSupoja.length < answers.length) {
            let j = 0
            while (subSupoja.length < answers.length) {
                subSupoja.push(subSupoja[j % subSupoja.length]);
                j++;
            }
        } else if (subSupoja.length > answers.length) {
            subSupoja = subSupoja.slice(0, answers.length)
        }

        answers.forEach((v, k) => {
            if (v === subSupoja[k]) {
                subAns += 1
            }
        })

        checkAns.push([i, subAns])
    }

    // 가장 큰 수 들을 뽑는다. 같으면 여러개를 다 뽑는다.
    const maxScore = Math.max(...checkAns.map(v => v[1]))

    // 필터링을 하여 큰 점수와 같은 idx 번호를 뽑는다.
    answer = checkAns.filter(v => v[1] === maxScore).map(v => v[0])

    return answer;
}

// 각 수포자가 찍는 방식 선언
// 정답과 각 수포자가 찍은 답을 확인하여 정답 개수를 확인
// 가장 많이 맞춘 사람을 골라낸다. 오름 차순으로

console.log(solution([1,2,3,4,5]))
console.log(solution([1,3,2,4,2]))