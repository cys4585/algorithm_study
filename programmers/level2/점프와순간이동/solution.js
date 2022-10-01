/*
* [2의 n제곱은 가는데 배터리 1소모]
* 1: 1 2 4 8 16 32 64 128 256 512 1024 2048 4096
* 5000 - 4096 = 904
* 2: 512
* 904 - 512 = 392
* 3: 256
* 392 - 256 = 136
* 4: 128
* 136 - 128 = 8
* 5: 8
*/

function solution(n) {
	let answer = 0;

	let teleport;
	while (n > 0) {
		answer++;
		teleport = 1;
		while (teleport <= n) teleport *= 2;
		n -= (teleport / 2);
	}
	return answer;
}

console.log(solution(5));
console.log(solution(6));
console.log(solution(5000));