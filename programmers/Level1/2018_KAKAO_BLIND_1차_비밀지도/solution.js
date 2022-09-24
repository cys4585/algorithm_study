function solution(n, arr1, arr2) {
    let answer = [];

	for (let i = 0; i < n; i++) {
		let [row1, row2] = [arr1[i].toString(2), arr2[i].toString(2)];
		row1 = '0'.repeat(n - row1.length) + row1;
		row2 = '0'.repeat(n - row2.length) + row2;
		let final_row = '';
		for (let j = 0; j < n; j++) {
			if (row1[j] === '0' && row2[j] === '0') final_row += ' ';
			else final_row += '#';
		}
		answer.push(final_row);
	}
    return answer;
}

console.log(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]));