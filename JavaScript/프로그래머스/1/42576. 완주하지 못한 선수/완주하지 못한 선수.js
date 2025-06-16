function solution(participant, completion) {
    var completeMap = completion.reduce((acc, name) => {
        if (acc.has(name)) {
            acc.set(name, acc.get(name) + 1);
        } else {
            acc.set(name, 1);
        }
        return acc;
    }, new Map())

    for (var idx = 0; idx < participant.length; ++idx) {
        var name = participant[idx];
        if (!completeMap.has(name) || completeMap.get(name) === 0) {
            return name
        }
        completeMap.set(name, completeMap.get(name) - 1);
    }
}