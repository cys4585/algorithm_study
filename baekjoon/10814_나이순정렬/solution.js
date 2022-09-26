function solution(arr) {
	arr.sort((a, b) => a[0] - b[0]).forEach(val => console.log(val.join(' ')));
}

function run(input) {
	let N = parseInt(input.shift());
	let arr = [];
	let i = 0;
	while (i < N)
		arr.push(input[i++].split(' ').map((val, idx) => idx === 0 ? parseInt(val) : val));
	solution(arr);
}

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
let input = [];
rl.on("line", function(line) {
    input.push(line)
}).on("close", function() {
    run(input);
    process.exit();
});