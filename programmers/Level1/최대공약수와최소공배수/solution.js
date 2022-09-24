function solution(n, m) {
    let answer = [];

	let greatestCommonFactor;
	let leastCommonMultiple =  n * m;
	if (n > m) [n, m] = [m, n];
	while (1) {
		if (m % n === 0) {
			greatestCommonFactor = n;
			break;
		}
		[m, n] = [n, m % n];
	} 
	leastCommonMultiple = leastCommonMultiple / greatestCommonFactor;
	answer = [greatestCommonFactor, leastCommonMultiple];
    return answer;
}

console.log(solution(72, 30));