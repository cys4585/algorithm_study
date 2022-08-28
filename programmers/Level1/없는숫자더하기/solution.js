function solution(numbers) {
	let answer = 0;
	
	for (let i = 1; i < 10; i++) answer += i;
	numbers.forEach(nbr => answer -= nbr)
    return answer;
}