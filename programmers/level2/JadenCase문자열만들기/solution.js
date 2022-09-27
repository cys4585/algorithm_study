function solution(s) {
    let answer = '';

	answer = s.split(' ')
		.map(word => word.split('').map((chr, idx) => idx === 0 ? chr.toUpperCase() : chr.toLowerCase()).join(''))
		.join(' ');
    return answer;
}

console.log(solution("3people unFollowed me"));
console.log(solution("for the last week"));