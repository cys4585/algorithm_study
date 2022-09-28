function solution(people, limit) {
    let answer = 0;

	people = people.sort((a, b) => b - a);
	for (let i = 0, j = people.length - 1; i <= j; i++) {
		if (limit - people[i] >= people[j])	j--;
		answer++;
	}
	return answer;
}

console.log(solution([70, 50, 80, 50], 100));
console.log(solution([70, 80, 50], 100));