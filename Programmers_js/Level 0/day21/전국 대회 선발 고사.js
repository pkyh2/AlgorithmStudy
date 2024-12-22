function solution(rank, attendance) {
  const randObj = {};
  const selection = [];
  rank.forEach((k, i) => {
    randObj[k] = [i, attendance[i]];
  });

  for (const key in randObj) {
    if (selection.length !== 3 && randObj[key][1]) {
      selection.push(randObj[key][0]);
    }
  }

  return 10000 * selection[0] + 100 * selection[1] + selection[2];
}

//
console.log(
  solution([3, 7, 2, 5, 4, 6, 1], [false, true, true, true, true, false, false])
);
console.log(
  solution([6, 1, 5, 2, 3, 4], [true, false, true, false, false, true])
);
