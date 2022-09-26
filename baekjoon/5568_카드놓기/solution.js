function rec(set, arr, visit, k, comb) {
	if (comb.length === k) set.add(comb.join(''));
	else
		for (let i = 0; i < arr.length; i++)
			if (visit[i] === false) {
				comb.push(arr[i]);
				visit[i] = true;
				rec(set, arr, visit, k, comb);
				comb.pop();
				visit[i] = false;
			}
}

function solution(k, arr) {
	let set = new Set();
	let visit = new Array(arr.length).fill(false);
	rec(set, arr, visit, k, new Array());
	console.log(set.size);
}

function run(input) {
	let n = parseInt(parseInt(input.shift()));
	let k = parseInt(parseInt(input.shift()));
	let arr = [];
	let i = 0;
	while (i < n)
		arr.push(parseInt(input[i++]));
	solution(k, arr);
}

const readline = require("readline");
const { compileFunction } = require("vm");
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