function solution(n) {
    let answer = 0;

	let ternary = '';
	while (n) {
		ternary += n % 3;
		n = parseInt(n / 3);
	}
	for (let power = 0; power < ternary.length; power++) 
		answer += ternary[ternary.length - power - 1] * (3 ** power);
    return answer;
}

console.log(solution(125));