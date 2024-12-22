function solution(date1, date2) {
  return new Date(date1) < new Date(date2) ? 1 : 0
}

console.log(solution([2021, 12, 28], [2021, 12, 29]));
console.log(solution([1024, 10, 24], [1024, 10, 24]));
console.log(solution([2022, 1, 1], [2021, 12, 31]));
console.log(solution([2023, 12, 1], [2023, 1, 23]));
console.log(solution([1999, 12, 31], [2000, 1, 23]));


// date1[0] < date2[0]
// date1[1] < date2[1]