function solution(N, edges, node1, node2) {
	let arr = [];
	for (let i = 0; i <= N; i++) arr[i] = {parent: null, childs: []};
	edges.forEach(([parent, child]) => {
		arr[parent].childs.push(child);
		arr[child].parent = parent;
	});
	let parentNode1 = [], parentNode2 = [];
	let node = node1;
	while (node !== null) {
		parentNode1.push(node);
		node = arr[node].parent;
	}
	node = node2;
	while (node !== null) {
		parentNode2.push(node);
		node = arr[node].parent;
	}
	console.log(parentNode1.find(node1 => parentNode2.find(node2 => node1 === node2)));
}

function run(input) {
	let T = parseInt(input[0]);
	let idx = 1;
	while (T--) {
		let N = parseInt(input[idx++]);
		let edges = [];
		let i = 0;
		while (i++ < N - 1)
			edges.push(input[idx++].split(' ').map(val => parseInt(val)));
		let nodes = input[idx++].split(' ').map(val => parseInt(val));
		solution(N, edges, ...nodes);
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