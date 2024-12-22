function solution(num_list) {
  let odd = '';
  let even = '';
  num_list.forEach((num, idx) => {
    if (num % 2 === 0) {
      even += num;
    } else {
      odd += num;
    }
  })
  return parseInt(even) + parseInt(odd);
}

console.log(solution([3, 4, 5, 2, 1]	)) // 1
console.log(solution([5, 7, 8, 3]	)) // 1