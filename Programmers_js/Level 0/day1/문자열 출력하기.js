// Node.js 내장 'readline' 모듈을 로드한다.
// 이 모듈은 인터랙티브한(실시간으로 상호 작용이 가능한 텍스트 기반) 커맨드 라인 인터페이스를 생성하는 데 사용된다.
const readline = require('readline');
const rl = readline.createInterface({
  // 터미널 또는 콘솔과 상호작용을 위해 'input', 'output' 스트림을 필요로 한다.
    input: process.stdin,
    output: process.stdout
});

// 입력 배열 초기화
// 사용자가 입력을 저장하기 위한 빈 배열을 선언
let input = [];


// 사용자가 새 줄에 입력을 완료 할 때마다 실행 된다.
// 입력 하고 엔터키를 누르면 'line' 이벤트가 발생하고 이 때마다 함수가 호출된다.
rl.on('line', function (line) {
    input = [line];
    // readline 인터페이스가 종료될 때 호출된다.
}).on('close',function(){
    str = input[0];
    console.log(str)
});