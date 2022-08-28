function pullUp (board, col, basket) {
	for (let row = 0; row < board.length; row++)
		if (0 < board[row][col]) {
			basket.push(board[row][col]);
			board[row][col] = 0;
			break;
		}
}

function checkBasket(basket) {
	if (2 <= basket.length && basket[basket.length - 1] === basket[basket.length - 2]) {
		basket.splice(basket.length - 2, 2);
		return 2;
	}
	return 0;
}

function solution(board, moves) {
	let answer = 0;
	let basket = [];
	
	moves.forEach(move => {
		pullUp(board, move - 1, basket);
		answer += checkBasket(basket);
	});
    return answer;
}
