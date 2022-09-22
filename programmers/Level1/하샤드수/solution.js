function solution(x) {
    let answer = true;

	let copy = x;
	let sum = 0;
	while (copy) {
		sum += copy % 10;
		copy = parseInt(copy / 10);
	}
	if (x % sum) answer = false;
    return answer;
}