function solution(brown, yellow) {
    let answer = [];

	let size = brown + yellow;
	for (let i = 3; i <= Math.sqrt(size); i++)
		if ((i - 2) * ((size / i) - 2) === yellow) {
			answer = [size / i, i];
			break;
		}
    return answer;
}

console.log(solution(10, 2));
console.log(solution(8, 1));
console.log(solution(24, 24));