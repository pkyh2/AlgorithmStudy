function solution(my_string, is_prefix) {
  return [...my_string]
    .map((char, i) => {
      return my_string.slice(0, i);
    })
    .includes(is_prefix)
    ? 1
    : 0;
}

console.log(solution("banana", "ban"));
