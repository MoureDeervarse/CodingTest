def solution(guest_amount, agent_list):
    min_time = guest_amount * min(agent_list) // len(agent_list)
    max_time = guest_amount * max(agent_list) // len(agent_list)
    lowerest_time = max_time
    
    while min_time < max_time:
        check_time = (min_time + max_time) // 2
        proceed_amount = sum([check_time // spd for spd in agent_list])
        if proceed_amount < guest_amount:
            # need more time
            min_time = check_time + 1
        else:
            # enough time
            lowerest_time = min(lowerest_time, check_time)
            max_time = check_time
            
    return lowerest_time
    