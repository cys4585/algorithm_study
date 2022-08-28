function solution(sizes) {
    let answer = 0;
    let wMax = 0
    let hMax = 0;
    let tmp;
    
    sizes.forEach(size => {
        if (size[0] < size[1]) {
            tmp = size[0];
            size[0] = size[1];
            size[1] = tmp;
        }
        if (wMax < size[0]) wMax = size[0];
        if (hMax < size[1]) hMax = size[1];
    });
    answer = wMax * hMax;
    return answer;
}