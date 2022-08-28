function solution(lottos, win_nums) {
    let answer = [];
    let maxExist;
    let minExist;
    let cntExistNbr = 0;
    let cntZero = 0;
    
    lottos.forEach(myNbr => {
        if (myNbr !== 0) {
            for (winNbr of win_nums) {
                if (myNbr === winNbr) {
                    cntExistNbr++;
                    break;
                }
            }
        }
        else cntZero++;
    });
    maxExist = cntExistNbr + cntZero;
    minExist = cntExistNbr;
    answer.push(maxExist < 2 ? 6 : 7 - maxExist);
    answer.push(minExist < 2 ? 6 : 7 - minExist);
    return answer;
}