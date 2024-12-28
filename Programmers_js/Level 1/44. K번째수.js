const solution = (array, commands) => {
  let result = []

  for (const v1 of commands) {
    const temp = array.slice(v1[0]-1, v1[1]).sort((a, b) => a - b)
    result.push(temp[v1[2]-1])

  }
  return result;
}


// 1. commands를 반복
// 2. 각 원소에서 idx 0, 1인 원소의 범위를 slice하여 새로운 배열 추출 한다.
// 3. 추출한 배열에서 idx 2 번째 수를 에 해당하는 원소 번째의 수를 최종 값에 저장

console.log(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))