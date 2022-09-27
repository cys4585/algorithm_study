function solution(s) {
    let answer = [];

	let prevLen;
	let cnt = 0, removeZero = 0;
	while (s !== '1') {
		prevLen = s.length;
		s = s.split('').filter(binary => binary === '1').join('');
		removeZero += (prevLen - s.length);
		s = parseInt(s.length).toString(2);
		cnt++;
	}
	answer = [cnt, removeZero];
    return answer;
}

console.log(solution("110010101001"));
console.log(solution("01110"));
console.log(solution("1111111"));