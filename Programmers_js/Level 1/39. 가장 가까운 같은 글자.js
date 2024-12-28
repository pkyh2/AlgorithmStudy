function solution(s) {
  var answer = [];
  let sArr = [...s]
  
  // s를 배열화 하여 반복
  sArr.forEach((v, i) => {
    // 원소 앞에 문자열을 뽑는다.
    const frontArr = [...s.slice(0, i)]

    // 뽑은 원소가 앞에 문자열에 있는지 확인
    if (frontArr.includes(v)) {
      const findIdx = []
      // 문자열에서 idx값을 모두 확인
      let index = frontArr.indexOf(v)
      while (index !== -1) {
        findIdx.push(index)
        index = frontArr.indexOf(v, index + 1)
      }

      // 현재 idx에서 문자열에서 뽑은 idx중 가장 큰값을 뺀다.
      answer.push(i - findIdx.pop())
    } else {
      // 뽑은 원소가 앞에 문자열에 없으면 -1을 대입한다.
      answer.push(frontArr.indexOf(v))
    }

  })
  return answer;
}


// 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자
// 처음 나온 수는 -1로 표현
// 같은 수가 반복 되면 가장 가까이 있는 수를 뺀다.
// 

// 1. 문자열을 배열화 시켜서 반복한다.
// 2. 각 원소를 뽑을 때 원소 앞에있는 문자열도 같이 뽑는다. slice()로
// 3. 뽑은 슬라이스에서 해당 원소를 포함하고 있는지 확인한다.
// 4. 포함하고 있으면 가장 큰 idx를 가진 수를 찾는다.
// 5. 찾은 원소와 현재 원소의 idx의 차이를 구한다. 그 값을 answer에 넣어준다.

console.log(solution("banana"))