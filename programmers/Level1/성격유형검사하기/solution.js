function solution(survey, choices) {
    const scores = {};
    const types = ["RT", "CF", "JM", "AN"];

    types.forEach((type) => type.split('').forEach((char) => scores[char] = 0));
    choices.forEach((choice, index) => {
        const [left, right] = survey[index];
        scores[choice > 4 ? right : left] += Math.abs(choice - 4);
    });
    const answer = types.map(([a, b]) => (scores[a] >= scores[b] ? a : b)).join('');
    return answer;
}

console.log(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))