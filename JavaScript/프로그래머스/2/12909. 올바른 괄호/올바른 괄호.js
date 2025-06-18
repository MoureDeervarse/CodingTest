function solution(s) {
    let count = 0;
    for (let idx = 0; idx < s.length; ++idx) {
        if (s[idx] === '(') {
            count++;
        } else if (count === 0) {
            return false;
        } else {
            count--;
        }
    }

    return count === 0;
}