function solution(n, words) {
    let answer = [0, 0];

	let usedWordSet = new Set();
	let turn = 1, currNum = 1;
	let prevWord = words[0][0];
	for (let word of words) {
		if (usedWordSet.has(word) || prevWord[prevWord.length - 1] !== word[0]) {
			answer[0] = currNum, answer[1] = turn;
			break;
		}
		usedWordSet.add(word);
		prevWord = word;
		currNum++;
		if (currNum > n) {
			currNum = 1;
			turn++;
		}
	}
    return answer;
}

console.log(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]));
console.log(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]));
console.log(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]));