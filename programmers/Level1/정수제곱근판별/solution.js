function solution(n) {
    let answer = 0;

	let sqrt = Math.sqrt(n);
	if (Number.isInteger(sqrt)) answer = (sqrt + 1)**2;
	else answer = -1;
    return answer;
}