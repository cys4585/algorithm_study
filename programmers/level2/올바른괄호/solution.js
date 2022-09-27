function solution(s){
    let answer = true;

	let cnt = 0;
	let arr = s.split('');
	for (let i = 0; i < arr.length; i++) {
		if (arr[i] === '(') cnt++;
		else {
			if (cnt === 0) return false;
			cnt--;
		}
	}
	if (cnt !== 0) answer = false;
    return answer;
}

console.log(solution("()()"));
console.log(solution("(())()"));
console.log(solution(")()("));
console.log(solution("(()("));