function solution(str_list) {
  const leftIdx = str_list.indexOf("l");
  const rightIdx = str_list.indexOf("r");
  if (leftIdx === -1 && rightIdx === -1) {
    return [];
  } else if (leftIdx === -1 || rightIdx === -1) {
    return leftIdx === -1
      ? str_list.slice(rightIdx + 1)
      : str_list.slice(0, leftIdx);
  } else {
    return leftIdx < rightIdx
      ? str_list.slice(0, leftIdx)
      : str_list.slice(rightIdx + 1);
  }
}

console.log(solution(["u", "u", "l", "r"]));
console.log(solution(["l"]));
console.log(solution(["u", "u", "r", "l", "r", "r", "r", "r"]));
