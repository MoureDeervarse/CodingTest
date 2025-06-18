function solution(arr) {
    if (arr.length === 0) {
        return [];
    }
    
    var answer = [arr[0]];
    for (let idx = 0; idx < arr.length; ++idx) {
        if (arr[idx] !== answer[answer.length-1]) {
            answer.push(arr[idx]);
        }
    }
    return answer;
}