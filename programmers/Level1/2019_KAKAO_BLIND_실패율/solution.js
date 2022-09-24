function solution(N, stages) {
    let answer = [];

	let stageInfos = [];
	for (let i = 1; i <= N; i++) {
		failRate = stages.filter(stage => stage === i).length / stages.filter(stage => stage >= i).length;
		if (isNaN(failRate)) failRate = 0;
		stageInfos.push({
			stage: i,
			failRate: failRate
		});
	}
	answer = stageInfos.sort((a, b) => a.failRate <= b.failRate ? -1 : 1).reverse().map(obj => obj.stage);
    return answer;
}

console.log(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]));
console.log(solution(4, [4,4,4,4,4]));
console.log(solution(5, [2, 1, 3, 5, 6, 6, 6]));
console.log(solution(5, [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4]));