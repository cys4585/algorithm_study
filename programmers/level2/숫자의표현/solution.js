function solution(n) {
    let answer = 1;

	for (let i = 1; i < n / 2; i++) {
		let sum = 0, j = i;
		while (sum < n) sum += j++;
		if (sum === n) {
			answer++;
			i++;
		}
	}
    return answer;
}

console.log(solution(15));