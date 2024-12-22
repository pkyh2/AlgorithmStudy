function solution(arr) {
  let cnt = 0;
  let beforeArr = arr;

  while (true) {
    let afterArr = [];
    beforeArr.map((num, i) => {
      if (num >= 50 && num % 2 === 0) {
        afterArr.push(parseInt(num / 2));
      } else if (num < 50 && num % 2 !== 0) {
        afterArr.push(num * 2 + 1);
      } else {
        afterArr.push(num);
      }
    });
    // 두 배열이 같으면
    if (beforeArr.every((v, i) => v === afterArr[i])) {
      break;
    } else {
      beforeArr = [...afterArr];
      cnt++;
    }
  }
  return cnt;
}

console.log(solution([1, 2, 3, 100, 99, 98]));
