/*
* 1칸 -> 1
* 2칸 -> 2
* 3칸 -> 3 (111 / 12 / 21)
* 4칸 -> 5 (1111 / 112 / 121 / 211 / 22)
* 5칸 -> 8 (11111 / 1112 / 1121 / 1211 / 2111 / 122 / 212 / 221)
* 6칸 -> 13 (111111 / 11112 11121 11211 12111 21111 / 1122 1212 1221 2112 2121 2211 / 222)
* f(n) = f(n - 2) + f(n - 1)
*/


function solution(n) {
	let answer = 0;

	let arr = [0, 1, 2];
	for (let i = 3; i <= n; i++)
		arr[i] = (arr[i - 2] + arr[i - 1]) % 1234567;
	answer = arr[n];
	return answer;
}


console.log(solution(4));
console.log(solution(3));
console.log(solution(2));