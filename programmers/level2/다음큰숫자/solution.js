function solution(n) {
    let answer = 0;

	let nBinaryOneCnt = n.toString(2).split('').filter(bin => bin === '1').length;
	let nextBinaryOneCnt;
	while (1) {
		n++;
		nextBinaryOneCnt = n.toString(2).split('').filter(bin => bin === '1').length;
		if (nBinaryOneCnt === nextBinaryOneCnt) break;
	}
	answer = n;
    return answer;
}

console.log(solution(78));
console.log(solution(15));