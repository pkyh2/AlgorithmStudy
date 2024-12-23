// function solution(arr1, arr2) {
//     let answer = []
//     if (arr1[0].length > 1) {
//         for (let i = 0; i < arr1.length; i++) {
//             answer.push(arr1.map((_, j) => arr1[i][j] + arr2[i][j]))
//         }
//     } else {
//         for (let i = 0; i < arr1.length; i++) {
//             answer.push([arr1[i][0] + arr2[i][0]])
//         }
//     }

//     return answer;
// }

const solution = (arr1, arr2) => {
    let answer = arr1

    for (let i = 0; i < arr1.length; i++) {
        for (let j = 0; j < arr1[i].length; j++) {
            answer[i][j] = arr1[i][j] + arr2[i][j]
        }
    }

    return answer
}

console.log(solution(
    [[1, 2], [2, 3]],
    [[3, 4], [5, 6]]
))

console.log(solution([[1], [2]], [[3], [4]]))

// arr1[0][0] + arr2[0][0]
// arr1[0][1] + arr2[0][1]
// arr1[1][0] + arr2[1][0]
// arr1[1][1] + arr2[1][1]
