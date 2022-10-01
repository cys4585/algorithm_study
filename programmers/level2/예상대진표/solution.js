/*
* cur -> next
* 1 2 -> 1 
* 3 4 -> 2 
* 5 6 -> 3 
* 7 8 -> 4
* 짝수 -> v/2
* 홀수 -> (v+1)/2
*/

/*
* a, b 값이 1 차이 && a, b 중 더 큰 값이 짝수 -> a, b 만남
*/

function solution(n,a,b) {
    let answer = 1;

	if (a > b) [a, b] = [b, a];
	while (!(a + 1 === b && b % 2 === 0)) {
		a = a % 2 ? (a + 1) / 2 : a / 2;
		b = b % 2 ? (b + 1) / 2 : b / 2;
		answer++;
	}
    return answer;
}

console.log(solution(8,4,7));