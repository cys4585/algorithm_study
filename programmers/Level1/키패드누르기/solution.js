function solution(numbers, hand) {
	let answer = "";
	let nbrPos = {
		1: [0, 0], 2: [0, 1], 3: [0, 2],
		4: [1, 0], 5: [1, 1], 6: [1, 2],
		7: [2, 0], 8: [2, 1], 9: [2, 2],
				   0: [3, 1]
	}
	let currPos = {"left": [3, 0], "right": [3, 2]}
	
	numbers.forEach(nbr => {
		if ([1, 4, 7].includes(nbr)) {
			answer += "L";
			currPos["left"] = nbrPos[nbr];
		}
		else if ([3, 6, 9].includes(nbr)) {
			answer += "R";
			currPos["right"] = nbrPos[nbr];
		}
		else {
			let [nextY, nextX] = nbrPos[nbr];
			let [currLY, currLX] = currPos["left"];
			let [currRY, currRX] = currPos["right"];
			let distanceLeft = Math.abs(nextY - currLY) + Math.abs(nextX - currLX);
			let distanceRight = Math.abs(nextY - currRY) + Math.abs(nextX - currRX);
			if (distanceLeft === distanceRight) {
				if (hand === "left") {
					answer += "L";
					currPos["left"] = nbrPos[nbr];
				}
				else {
					answer += "R";
					currPos["right"] = nbrPos[nbr];
				}
			}
			else if (distanceLeft < distanceRight) {
				answer += "L";
				currPos["left"] = nbrPos[nbr];
			}
			else {
				answer += "R";
				currPos["right"] = nbrPos[nbr];
			}
		}
	})
    return answer;
}
console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"));