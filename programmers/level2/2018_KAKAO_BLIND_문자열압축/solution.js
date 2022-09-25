function solution(s) {
    let answer = 1;

	let compressed = [];
	let compressedLen;
	let cnt;
	for (let unit = 1; unit < s.length; unit++) {
		cnt = 1;
		for (let i = 0; i < s.length; i += unit) {
			let [curr, next]= [s.substring(i, i + unit), s.substring(i + unit, i + 2 * unit)];
			if (curr === next) cnt++;
			else {
				if (cnt > 1) compressed.push(cnt + curr);
				else if (cnt === 1) compressed.push(curr);
				cnt = 1;
			}
		}
		compressedLen = compressed.join('').length;
		compressed = [];
		if (answer === 1 || compressedLen < answer) answer = compressedLen;
	}
    return answer;
}

console.log(solution("aabbaccc"));
console.log(solution("ababcdcdababcdcd"));
console.log(solution("abcabcdede"));
console.log(solution("abcabcabcabcdededededede"));
console.log(solution("xababcdcdababcdcd"));
console.log(solution('a'));