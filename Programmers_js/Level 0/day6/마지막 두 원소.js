function solution(num_list) {
  var answer = num_list;
  const lastNum = num_list[num_list.length-1]
  const lastSecondNum = num_list[num_list.length-2]
  if (lastNum > lastSecondNum) {
    answer.push(lastNum - lastSecondNum);
  } else {
    answer.push(lastNum * 2)
  }
  return answer;
}

console.log(solution([3, 4, 5, 2, 1]	)) // 1
console.log(solution([2, 1, 6]	)) // 1
console.log(solution([5, 2, 1, 7, 5]	)) // 1