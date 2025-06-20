function solution(clothes) {
    const res = clothes.reduce((dict, val) => {
        const category = val[1];
        dict[category] = category in dict ? dict[category] + 1 : 2;
        return dict;
    }, {});
    return Object.values(res).reduce((mul, val) => mul * val, 1) - 1;
}