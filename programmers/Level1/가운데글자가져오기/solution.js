function solution(s) {
    let answer = '';

	if (s.length % 2) answer = s.charAt(parseInt(s.length / 2));
	else answer = s.substring(s.length / 2 - 1, s.length / 2 + 1);
    return answer;
}