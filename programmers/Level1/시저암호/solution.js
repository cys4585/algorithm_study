function solution(s, n) {
    let answer = '';

	// ascii code
	// 대문자: 65 ~ 90
	// 소문자: 97 ~ 122
	answer = s.split('').map(char => {
		if (char === ' ') return char;
		let push_ascii = char.charCodeAt() + n;
		if (('a' <= char && char <= 'z') && (97 <= push_ascii && push_ascii <= 122))
			return String.fromCharCode(push_ascii);
		else if (('A' <= char && char <= 'Z') && (65 <= push_ascii && push_ascii <= 90))
			return String.fromCharCode(push_ascii);
		return String.fromCharCode(push_ascii - 26);
	}).join('');
    return answer;
}

console.log(solution("a   B w", 4));