function solution(s){
    let answer = true;

	let cnt = 0;
	for (let i = 0; i < s.length; i++) {
		if (s[i] === 'p' || s[i] === 'P') cnt++;
		else if (s[i] === 'y' || s[i] === 'Y') cnt--;
	}
	if (cnt !== 0) answer = false;
    return answer;
}