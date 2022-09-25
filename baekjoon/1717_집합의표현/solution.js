function find(arr, v) {
	if (arr[v] !== v) return arr[v] = find(arr, arr[v]);
	return v;
}

function union(arr, a, b) {
	if (a === b) return;
	a = find(arr, a);
	b = find(arr, b);
	arr[b] = a;
}

function run(input) {
	let n = parseInt(input[0].split(' ')[0]);
	let arr = new Array(n + 1);
	for (let i = 0; i <= n; i++) arr[i] = i;
	let flag, a, b;
	for (let i = 1; i < input.length; i++) {
		[flag, a, b] = input[i].split(' ').map(val => parseInt(val));
		if (flag === 0) union(arr, a, b);
		else
			if (find(arr, a) === find(arr, b)) console.log('YES');
			else console.log('NO');
	}
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