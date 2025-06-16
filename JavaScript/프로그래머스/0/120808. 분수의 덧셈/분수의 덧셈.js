function solution(numer1, denom1, numer2, denom2) {
    var lcm = getLCM(denom1, denom2);
    var multiple1 = lcm / denom1;
    var multiple2 = lcm / denom2;
    var numer_total = numer1 * multiple1 + numer2 * multiple2
    var gcd = getGCD(numer_total, lcm)
    return [numer_total / gcd, lcm / gcd];
}

function getGCD(a, b) {
    while (b) {
        const temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

function getLCM(a, b) {
    if (a === 0 || b === 0) {
        return 0;
    }
    return a * b / getGCD(a, b);
}