function solution(my_string) {
  return [...my_string]
    .map((char, i) => {
      return my_string.slice(i);
    })
    .sort();
}

console.log(solution("programmers"));
