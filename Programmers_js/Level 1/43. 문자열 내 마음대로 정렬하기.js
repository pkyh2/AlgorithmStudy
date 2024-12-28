// function solution(strings, n) {
//   var answer = [];
//   const str = {}
//   strings.forEach((v, i) => {
//     str[i] = v[n]
//   })

//   const sortedObj = Object.entries(str) // 객체를 배열로 변환: [["0", "u"], ["1", "e"], ["2", "a"]]
//   .sort(([, valueA], [, valueB]) => valueA.localeCompare(valueB)) // value 기준으로 정렬
//   console.log("🚀 ~ solution ~ sortedObj:", JSON.stringify(sortedObj))


//   const sortedWord = []
//   for (const v of sortedObj) {
//     // 순서가 같은 원소 정렬
//     sortedWord.push(strings[Number(v[0])])
//   }

//   answer = sortPartial(sortedWord, sortedObj[0])

//   return answer;
// }


// function sortPartial(arr, start, end) {
//   return [
//     ...arr.slice(0, start).sort(),            // 정렬 이전의 원소 유지
//     ...arr.slice(start, end).sort(),  // 정렬 대상 범위 정렬
//     ...arr.slice(end).sort() 
//   ]
// }

// 1. 배열을 반복하면서 n번째 원소들을 추출하여 idx와 같이 객체를 만든다.\
// 2. 만든 객체를 알파벳에 따라 정렬한다.
// 3. answer에 정렬한 객체의 value값에 순서에 따라 strings의 원소값을 넣는다.




// 1. sort() 메서드를 이용하여 n번째 글짜를 비교하면 되는구나
// 2. localeCompare() => 
/*
"a"는 "c"의 앞에 오기 때문에 음수 값을 리턴
'a'.localeCompare('c'); // -2 or -1 (or some other negative value)

알파벳 순으로 "check"는 "against"의 뒤에 오기 때문에 양수 값을 리턴
'check'.localeCompare('against'); // 2 or 1 (or some other positive value)

"a"는 "a"와 같기 때문에 0
'a'.localeCompare('a'); // 0
*/
const solution = (strings, n) => {
  return strings.sort((a, b) => a[n] === b[n] ? a.localeCompare(b) : a[n].localeCompare(b[n]))
}

console.log(solution(["sun", "bed", "car"], 1))
console.log(solution(["abce", "abcd", "cdx"], 2))