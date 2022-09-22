function solution(arr) {
    let answer = 0;

	answer = arr.reduce((prev, curr) => prev + curr) / arr.length;
    return (answer);
}
