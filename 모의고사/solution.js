function solution(answers) {
	let result = [];
	let	correctCount = [0, 0, 0];
	let patternArr = [
		[1, 2, 3, 4, 5],
		[2, 1, 2, 3, 2, 4, 2, 5],
		[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
	];

	patternArr.forEach((pattern, i) => {
		answers.forEach((answer, j) => {
			if (answer === pattern[j % pattern.length])
				correctCount[i]++;
		});
	});
	let max = Math.max(...correctCount);
	correctCount.forEach((cnt, idx) => {
		if (cnt === max)
			result.push(idx + 1);
	});
    return result;
}

// expect: [1]
console.log(solution([1,2,3,4,5]));