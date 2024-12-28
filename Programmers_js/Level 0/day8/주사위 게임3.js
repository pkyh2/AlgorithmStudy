function solution1(a, b, c, d) {
  const arr = [a, b, c, d];
  const arrSort = arr.sort();
  console.log("🚀 ~ solution ~ arrSort:", arrSort);

  // case1
  if (arrSort.every((v) => v === arrSort[0])) return 1111 * a;

  // case2
  if (arrSort.filter((v) => v === arrSort[0]).length === 3) {
    return (10 * arrSort[0] + arrSort[3]) ** 2;
  } else if (arrSort.filter((v) => v === arrSort[3]).length === 3) {
    return (10 * arrSort[3] + arrSort[0]) ** 2;
  }

  // case3
  if (
    arrSort.filter((v) => v === arrSort[0]).length === 2 &&
    arrSort.filter((v) => v === arrSort[2]).length === 2
  ) {
    return (arrSort[1] + arrSort[2]) * Math.abs(arrSort[1] - arrSort[2]);
  }

  //case4
  if (arrSort.filter((v) => v === arrSort[0]).length === 2) {
    return arrSort[2] * arrSort[3];
  } else if (arrSort.filter((v) => v === arrSort[3]).length === 2) {
    return arrSort[0] * arrSort[1];
  } else if (arrSort.filter((v) => v === arrSort[1]).length === 2) {
    return arrSort[0] * arrSort[3];
  }

  // case5
  if (new Set(arrSort).size === 4) return arrSort[0];
}

function solution(a, b, c, d) {
  const arr = [a, b, c, d].sort();
  // case1
  if (arr.every((v) => v === a)) return a * 1111;

  // case2
  if (
    (arr[0] !== arr[1] && arr[1] === arr[3]) ||
    (arr[0] === arr[2] && arr[2] !== arr[3])
  ) {
    const triple = arr[0] === arr[1] ? arr[0] : arr[3];
    const signle = arr[0] === arr[1] ? arr[3] : arr[0];
    return (10 * triple + signle) ** 2;
  }

  // case3
  if (arr[0] === arr[1] && arr[2] === arr[3]) {
    return (arr[1] + arr[2]) * Math.abs(arr[1] - arr[2]);
  }

  // case4
  if (arr[0] === arr[1]) return arr[2] * arr[3];
  else if (arr[2] === arr[3]) return arr[0] * arr[1];
  else if (arr[1] === arr[2]) return arr[0] * arr[3];

  // case5
  if (new Set(arr).size === 4) return arr[0];
}

// 1, 11, 16, 24, 36, 39
console.log(solution(2, 2, 2, 2));
console.log(solution(4, 1, 4, 4));
console.log(solution(6, 3, 3, 6));
console.log(solution(2, 5, 2, 6));
console.log(solution(6, 4, 2, 5));
console.log(solution(2, 2, 1, 4));
