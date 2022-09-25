function cmpWS(Walphabet, Salphabet) {
	for (let chr in Walphabet)
		if (Walphabet[chr] !== Salphabet[chr]) return false;
	return true;
}

function solution(input) {
	let [lengths, W, S] = input;
	W = W.split('');
	lengths = lengths.split(' ');
	let g = parseInt(lengths[0]), s = parseInt(lengths[1]);

	let alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	let Walphabet = {};
	let Salphabet = {};
	for (let chr of alphabet) Walphabet[chr] = 0, Salphabet[chr] = 0;
	for (let i = 0; i < g; i++)	Walphabet[W[i]]++;
	
	let cnt = 0, len = 0, idx = 0;
	for (let i = 0; i <= s; i++) {
		Salphabet[S[i]]++;
		len++;
		if (len === g) {
			if(cmpWS(Walphabet, Salphabet)) cnt++;
			len--;
			Salphabet[S[idx++]]--;
		}
	}
	console.log(cnt);
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
    solution(input);
    process.exit();
});