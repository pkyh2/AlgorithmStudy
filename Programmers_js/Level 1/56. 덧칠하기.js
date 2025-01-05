const solution1 = (n, m, section) => {
    const minEle = section[0]
    const maxEle = section[section.length - 1]
    const len = Math.ceil((maxEle - minEle + 1) / m)
    if (len === 1) return 1

    let temp = section
    let cnt = 0
    for (let i = 0; i < len; i++) {
        const left = minEle + (m * i)
        const right = minEle + (m - 1) + (m * i)
        const tempArr = Array.from({length: right - left + 1}, (_, i) => i + left)
        const isEle = temp.filter(item => tempArr.includes(item)).length

        if (temp.length !== 0 && isEle !== 0) {
            // console.log(temp)
            temp = temp.filter(item => !tempArr.includes(item))

            cnt += 1
        }


    }
    return cnt
}

const solution2 = (n, m, section) => {
    let arr = Array.from({length: n}, (_, i) => i + 1).slice(section[0]-1).filter(item => item <= section[section.length - 1])
    const len = Math.ceil(arr.length / m)
    let cnt = 0
    for (let i = 0; i < len; i++) {
        // const temp = arr.slice((m*i), m + (m*i))
        const temp = arr.slice(0, m)
        const intersection = temp.filter(item => section.includes(item)).length

        if (intersection !== 0) cnt += 1
        
        arr = arr.slice(m)
        console.log("🚀 ~ solution ~ arr:", arr) //이거 맞아 이대로 좀만더 생각해보자
    }
    return cnt
}

const solution3 = (n, m, section) => {
    let arr = Array.from({length: n}, (_, i) => i + 1).slice(section[0]-1).filter(item => item <= section[section.length - 1])
    let cnt = 0

    while (arr.length !== 0) {
        const temp = arr.slice(0, m)
        console.log("🚀 ~ solution ~ section:", section)
        if (temp.includes(section[0])) {
            cnt += 1
            console.log("🚀 ~ solution ~ arr:", arr)
            arr = arr.slice(m)
        } else {
            section.shift()
        }
    }

    for (let i = 0; i < section.length; i++) {
        const temp = arr.slice(0, m)
        if (temp.includes(section[i])) {
            cnt += 1
            arr = arr.slice(m).includes(section[i+1]) ? arr.slice(m) : arr
        } else {
            continue;
        }
    }

    return cnt
}

const solution = (n, m, section) => {
    let wall = Array.from({length: n}, (_, i) => i + 1)
    let cnt = 0

    section.forEach((v) => {
        wall[wall.indexOf(v)] = 0
    }) 

    for (let i = 0; i < wall.length; i++) {
        if (wall[i] === 0) {
            for (let j = 0; j < m; j++) {
                wall[i + j] = 1
            }
            cnt += 1
        }
    }
    return cnt
}

// 1. n 길이의 벽 생성
// 2. n / m 만큼 반복
// 3. 칠하는 범위에 section 값이 있으면 cnt += 1

console.log(solution(8, 4, [2, 3, 6]))
console.log(solution(5, 4, [1, 3]))
console.log(solution(4, 1, [1, 2, 3, 4]))
console.log(solution(10, 4, [6, 10]))
console.log(solution(5, 2, [1, 5]))
console.log(solution(10, 3, [1, 3, 6, 7])) // 중간
/*
길이가 n
1미터 길이의 구역 n개로 나누고
각 구역의 왼쪽부터 순서대로 1번 부터 ㅜn번까지 번호를 붙임.
롤러의 길이 m


*/
