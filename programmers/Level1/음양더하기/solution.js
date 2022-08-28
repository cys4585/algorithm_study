function solution(absolutes, signs) {
	let answer = 0;
	let sign = 1;

	for (let i = 0; i < absolutes.length; i++) {
		if (signs[i]) sign = 1;
		else sign = -1;
		answer += absolutes[i] * sign;
	}
    return answer;
}
console.log(solution([4,7,12], [true, false, true]));