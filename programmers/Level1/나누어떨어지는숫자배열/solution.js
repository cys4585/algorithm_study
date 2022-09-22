function solution(arr, divisor) {
    let answer = [];

	answer = arr.filter(nbr => !(nbr % divisor)).sort((a, b) => a - b);
	if (!answer.length) answer.push(-1);
    return answer;
}