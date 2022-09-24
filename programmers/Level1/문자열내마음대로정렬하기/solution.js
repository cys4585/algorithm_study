function solution(strings, n) {
    let answer = [];

	answer = strings.sort((a, b) => {
		let [ca, cb] = [a[n], b[n]];
		if (ca === cb) return a < b ?  -1 : 1;
		return ca < cb ? -1 : 1;
	});
    return answer;
}

console.log(solution(["sun", "bed", "car"], 1));