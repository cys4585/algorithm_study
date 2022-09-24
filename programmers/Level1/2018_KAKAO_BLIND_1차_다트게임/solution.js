function getInfo(str) {
	if (str.length === 2)
		return [parseInt(str[0]), str[1], null];
	else if (str.length === 3)
		if (str[1] === '0') return [parseInt(str[0] + str[1]), str[2], null];
		else return [parseInt(str[0]), str[1], str[2]];
	else if (str.length === 4)
		return [parseInt(str[0] + str[1]), str[2], str[3]];
}

function solution(dartResult) {
    let answer = 0;

	let dartResultList = [];
	let startIdx = 0
	for (let i = 2; i < dartResult.length; i++)
		if ('0' <= dartResult[i] && dartResult[i] <= '9') {
			dartResultList.push(dartResult.substring(startIdx, i));
			startIdx = i++;
		}
	dartResultList.push(dartResult.substring(startIdx));

	let pointList = [0,0,0];
	console.log(dartResultList);
	dartResultList.forEach((str, idx) => {
		let [point, bonus, option] = getInfo(str);
		if (bonus === 'D') point **= 2;
		else if (bonus === 'T') point **= 3;
		if (option === '*') {
			point *= 2;
			if (idx !== 0) pointList[idx - 1] *= 2;
		} else if (option === '#') point = -point;
		pointList[idx] = point;
	});
	answer = pointList.reduce((a, b) => a + b);
    return answer;
}

console.log(solution('1S2D*3T'));
console.log(solution('1D2S#10S'));
console.log(solution('1D2S0T'));
console.log(solution('1S*2T*3S'));
console.log(solution('1D#2S*3S'));
console.log(solution('1T2D3D#'));
console.log(solution('1D2S3T*'));
console.log(solution('10D10S0D'));