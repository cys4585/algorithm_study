function solution(arr) {
    let answer = [];

	arr.splice(arr.indexOf(Math.min(...arr)), 1);
	answer = arr.slice();
	if (!answer.length) answer.push(-1);
    return answer;
}