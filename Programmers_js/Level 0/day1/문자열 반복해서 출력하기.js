const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    str = input[0];
    n = Number(input[1]);
    for(i=0; i < n; i++) {
      // process.stdout.write() -> Node.js에서 표준 출력 스트림(stdout)에 직접 데이터를 쓰는 데 사용되는 메서드
      // process는 Node.js의 
      rl.output.write(str)
    }
});