function solution(price, money, count) {
    let answer = 0;

	let total_price = 0;
	for (let n = 1; n <= count; n++)
		total_price +=  price * n;
	if (money < total_price) answer = total_price - money;
    return answer;
}

console.log(solution(3, 20, 4));