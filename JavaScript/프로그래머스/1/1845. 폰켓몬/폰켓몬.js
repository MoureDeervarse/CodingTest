function solution(nums) {
    var answer = 0;
    const results = nums.reduce((cur, val) => {
        if (!(val in cur)) {
            cur[val] = 1;
        }
        return cur;
    }, {});
    return Math.min(Object.keys(results).length, nums.length/2);
}