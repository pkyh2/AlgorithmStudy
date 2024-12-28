function solution(todo_list, finished) {
  var answer = todo_list.filter((todo, idx) => {
    if (finished[idx] === false) {
      return todo;
    }
  });
  return answer;
}

console.log(
  solution(
    ["problemsolving", "practiceguitar", "swim", "studygraph"],
    [true, false, true, false]
  )
);
