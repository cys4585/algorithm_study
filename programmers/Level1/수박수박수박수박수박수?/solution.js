function solution(n) {
    let answer = '';

	let char = '수';
	for (let i = 0; i < n; i++) {
		answer += char;
		if (char === '수') char = '박';
		else char = '수';
	}
    return answer;
}