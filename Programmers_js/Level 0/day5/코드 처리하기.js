function solution(code) {
  var ret = '';
  let mode = 0;

  for(let i=0; i<code.length; i++) {
    if (mode === 0) {
      if (code[i] === "1") {
        mode = 1;
      } else if (i % 2 === 0) {
        ret += code[i];
      }
    } else if (mode === 1) {
      if (code[i] === "1") {
        mode = 0;
      } else if (i % 2 === 1) {
        ret += code[i];
      }
    }
  }
  return ret ? ret : "EMPTY";
}


const solution = (code) => {
  let ret = '';
  let mode = 0;

  for (let i = 0; i < code.length; i++) {
    if (code[i] === '1') {
      mode = 1 - mode;
    } else if ((mode === 0 && i % 2 === 0) || (mode === 1 && i % 2 === 1)) {
      ret += code[i];
    }
  }

  return ret ? ret : 'EMPTY';
}

console.log(solution("abc1abc1abc"))

// 앞에서 부터 읽으면서 문자가 1이면 mode를 바꾼다.
// mode는 0과 1이 있다.

// mode가 0일 때 code[idx]가 "1"이 아니면 idx가 짝수 일 때만 ret의 맨 뒤에 code[idx]를 추가한다.
// mode 시작이 0 


//구현해야될 것들