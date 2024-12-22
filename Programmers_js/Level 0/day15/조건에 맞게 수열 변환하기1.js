function solution(arr) {
  var answer = [];
  arr.forEach((num, i) => {
    if (num % 2 === 0 && num >= 50) {
      answer.push(parseInt(num / 2));
    } else if (num % 2 !== 0 && num < 50) {
      answer.push(num * 2);
    } else {
      answer.push(num);
    }
  });
  return answer;
}

console.log(solution([1, 2, 3, 100, 99, 98]));
