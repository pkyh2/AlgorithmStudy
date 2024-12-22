function solution(my_string, overwrite_string, s) {
  var answer = '';
  answer = my_string.slice(0, s) + overwrite_string + my_string.slice(s+overwrite_string.length)
  return answer;
}

const my_string = "He11oWor1d"
const overwrite_string = 	"lloWorl"
const s = 2
console.log(solution(my_string, overwrite_string, s))
const my_string1 = "Program29b8UYP"
const overwrite_string1 = 	"merS123"
const s1 = 7
console.log(solution(my_string1, overwrite_string1, s1))