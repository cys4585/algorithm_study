function solution(a, b) {
    let answer = '';

	let month_date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
	let dayOfTheWeek = ["FRI","SAT","SUN","MON","TUE","WED","THU"];
	let date = b - 1;
	for (let i = 0; i < a - 1; i++)	date += month_date[i];
	answer = dayOfTheWeek[date % 7];
    return answer;
}

console.log(solution(5, 24));