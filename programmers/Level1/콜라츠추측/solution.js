function solution(num) {
    let answer = 0;

	while (num !== 1) {
		if (num % 2) num = num * 3 + 1;
		else num = parseInt(num / 2);
		if (answer === 500) return -1;
		answer++;
	}
    return answer;
}