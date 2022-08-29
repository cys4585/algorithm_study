function solution(participant, completion)
{
	let answer = '';
	let hash = {};

	participant.forEach(name => hash[name] = 0);
	participant.forEach(name => hash[name] += 1);
	completion.forEach(name => hash[name] -= 1);
	for (let [name, value] of Object.entries(hash))
		if (value !== 0)
		{
			answer = name;
			break;
		}
    return answer;
}

// expect "leo"
console.log(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]));