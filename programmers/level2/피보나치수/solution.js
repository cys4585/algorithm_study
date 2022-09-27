function solution(n) {
	let answer = 0;

	let fn_2 = 0, fn_1 = 1;
	for (let i = 2; i <= n; i++) {
		answer = (fn_2 + fn_1) % 1234567;
		fn_2 = fn_1;
		fn_1 = answer;
	}
	return answer;
}

console.log(solution(3));
console.log(solution(5));