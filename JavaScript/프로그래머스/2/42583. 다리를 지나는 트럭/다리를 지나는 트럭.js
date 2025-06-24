function solution(bridge_length, weight, truck_weights) {
    let sec = 0;
    let cur_weight = 0;
    const bridge = [];
    
    while (truck_weights.length > 0 || bridge.length > 0) {
        if (bridge.length > 0 && bridge[0].arrival_sec === sec) {
            const arrival_truck = bridge.shift();
            cur_weight -= arrival_truck.truck_weight;
        }
        if (truck_weights.length > 0) {
            const is_enough_weight = cur_weight + truck_weights[0] <= weight;
            const is_enough_space = bridge.length < bridge_length;
            if (is_enough_weight && is_enough_space) {
                const truck_weight = truck_weights.shift();
                bridge.push({
                    arrival_sec: sec + bridge_length, 
                    truck_weight: truck_weight,
                });
                cur_weight += truck_weight;
            }
        }
        sec++;
    }
    return sec;
}