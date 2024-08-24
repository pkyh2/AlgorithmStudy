function solution(num_list) {
  let cnt = 0;
  for (num of num_list) {
    let temp = num;
    while (true) {
      if (temp === 1) break;
      else if (temp % 2 === 0) {
        temp = parseInt(temp / 2);
      } else if (temp % 2 !== 0) {
        temp = parseInt((temp - 1) / 2);
      }
      cnt++;
    }
  }
  return cnt;
}

console.log(solution([12, 4, 15, 1, 14]));
