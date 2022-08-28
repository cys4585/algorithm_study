function solution(array, commands) {
    let answer = [];
    
    answer = commands.map(([start, end, key]) => {
      return array.slice(start - 1, end).sort((a, b) => a - b)[key - 1];
    })
    return answer;
  }