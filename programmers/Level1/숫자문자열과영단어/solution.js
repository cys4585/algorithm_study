function solution(s) {
	let answer = 0;
	let answerList = [];
	let nbrList = [
		"zero", "one", "two", "three", "four", 
		"five", "six", "seven", "eight", "nine"
	];

	let tmp = "";
	for (let i = 0; i < s.length; i++) {
		if (!isNaN(s[i])) answerList.push(Number(s[i]));
		else {
			let j = i;
			while (isNaN(s[j]) && !nbrList.includes(tmp))
				tmp += s[j++];
			answerList.push(nbrList.indexOf(tmp));
			i = j - 1;
			tmp = "";
		}
	}
	answer = Number(answerList.join(""));
    return answer;
}