function solution(nums) {
    let answer = 0;
	let sumVal = 0;
	let	isPrime;
	
	for (let i = 0; i < nums.length - 2; i++)
		for (let j = i + 1; j < nums.length - 1; j++)
			for (let k = j + 1; k < nums.length; k++) {
				sumVal = nums[i] + nums[j] + nums[k];
				isPrime = true;
				for (let l = 2; l <= Math.sqrt(sumVal); l++)
					if (sumVal % l === 0) {
						isPrime = false;
						break;
					}
				if (isPrime)
					answer++;
			}
    return answer;
}