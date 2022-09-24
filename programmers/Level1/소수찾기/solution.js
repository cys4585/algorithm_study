function isPrimeNumber(nbr) {
	if (nbr === 2) return true;
	for (let i = 2; i <= Math.sqrt(nbr); i++)
		if (nbr % i === 0) return false;
	return true;
}

function solution(n) {
	let answer = 0;

	for (let i = 2; i <= n; i++)
		if (isPrimeNumber(i)) answer++;
	return answer;
}

console.log(solution(10));
console.log(solution(5));