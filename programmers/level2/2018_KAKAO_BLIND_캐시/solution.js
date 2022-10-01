// LRU(Least Recently Used): 가장 오랫동안 참조되지 않은 페이지 삭제

function solution(cacheSize, cities) {
    let answer = 0;

	let HIT = 1, MISS = 5;
	let cacheArr = [];
	cities.forEach(city => {
		city = city.toLowerCase(city);
		if (cacheArr.includes(city)) {
			answer += HIT;
			cacheArr.splice(cacheArr.indexOf(city), 1);
		}
		else answer += MISS;
		cacheArr.push(city);
		if (cacheArr.length > cacheSize) cacheArr.shift();
	});
    return answer;
}

console.log(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]));
console.log(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]));
console.log(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]));
console.log(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]));
console.log(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]));
console.log(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]));