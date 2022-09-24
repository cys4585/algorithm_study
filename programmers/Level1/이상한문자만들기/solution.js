function solution(s) {
    let answer = '';

	answer = s.split(' ')
		.map(word => word.split('').map((char, index) => index % 2 ? char.toLowerCase() : char.toUpperCase()).join(''))
		.join(' ');
    return answer;
}

console.log(solution('try hello world'));