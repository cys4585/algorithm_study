function solution(nums) {
	let answer = 0;
	let pocket = [];

	for (let nbr of nums) {
		if (!pocket.includes(nbr)) {
			pocket.push(nbr);
			answer++;
		}
		if (answer === nums.length/2) break;
	}
	return answer;
}