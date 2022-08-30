function solution(n, lost, reserve) {
	let answer = 0;
	let students = {};

	for (let i = 1; i <= n; i++)
		students[i] = {lost: 0, reserve: 0};
	lost.forEach(nbr => students[nbr].lost = 1);
	reserve.forEach(nbr => students[nbr].reserve = 1);
	for (const nbr of Object.keys(students))
	{
		if (students[nbr].lost === 1 && students[nbr].reserve === 1)
		{
			students[nbr].lost = 0;
			students[nbr].reserve = 0;
		}
	}
	for (const nbr of Object.keys(students))
	{
		if (Number(nbr) > 1 && students[nbr].lost === 1 && students[Number(nbr) - 1].reserve === 1)
		{
			students[nbr].lost = 0;
			students[Number(nbr) - 1].reserve = 0;
		}
		else if (Number(nbr) < n && students[nbr].lost === 1 && students[Number(nbr) + 1].reserve === 1)
		{
			students[nbr].lost = 0;
			students[Number(nbr) + 1].reserve = 0;
		}
	}
	answer = n;
	for (let nbr in students)
		answer -= students[nbr].lost;
    return answer;
}

// 1 2 3 4 5 6
//     l l l
//     r r   r

console.log(solution(6, [3,4,5], [3,4,6]))