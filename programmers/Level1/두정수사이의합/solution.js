function solution(a, b) {
    let answer = 0;

	if (a === b) return a;
	if (b < a) [a, b] = [b, a];
	while (a <= b) {
		answer += a++;
	}
    return answer;
}
