function solution(arr) {
    let answer = 0;

	let maxNbr = Math.max(...arr);
	let multiple = 1;
	while (1) {
		answer = maxNbr * multiple;
		if (arr.every(nbr => answer % nbr === 0)) break;
		multiple++;
	}
    return answer;
}

console.log(solution([2,6,8,14]));
console.log(solution([1,2,3]));