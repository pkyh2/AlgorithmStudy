function solution(arr) {
  if (!arr.includes(2)) return [-1];
  let indices = [];
  arr.forEach((num, i) => {
    if (num === 2) {
      indices.push(i);
    }
  });
  return arr.slice(indices[0], indices.at(-1) + 1);
}

console.log(solution([1, 2, 1, 4, 5, 2, 9]));
console.log(solution([1, 1, 1]));
console.log(solution([1, 2, 1, 2, 1, 10, 2, 1]));
