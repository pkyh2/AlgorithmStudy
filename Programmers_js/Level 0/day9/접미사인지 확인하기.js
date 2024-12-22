function solution(my_string, is_suffix) {
  return [...my_string]
    .map((char, i) => {
      return my_string.slice(i);
    })
    .includes(is_suffix)
    ? 1
    : 0;
}

console.log(solution("banana", "ana"));
