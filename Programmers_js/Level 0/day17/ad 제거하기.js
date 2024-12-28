const solution = (strArr) => {
  return strArr.filter((arr, i) => !arr.includes("ad"));
};

console.log(solution(["and", "notad", "abcd"]));
