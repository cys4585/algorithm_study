function solution(s) {
    let answer = false;

	if (s.length == 4 || s.length == 6) 
		if (s.split('').filter(c => ('9' < c || c < '0')).length == 0) 
			answer = true;
    return answer;
}

console.log(solution("1234"));