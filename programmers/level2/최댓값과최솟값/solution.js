function solution(s) {
    let answer = '';

	let arr = s.split(' ');
	let min = Math.min(...arr);
	let max = Math.max(...arr);

	answer = min + ' ' + max;
    return answer;
}

console.log(solution("1 2 3 4"));
console.log(solution("-1 -2 -3 -4"));
console.log(solution("-1 -1"));