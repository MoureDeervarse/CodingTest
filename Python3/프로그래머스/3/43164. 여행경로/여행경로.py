def solution(tickets):
    remain_ticket_map = {}
    for ticket_info in tickets:
        start, dest = ticket_info[0], ticket_info[1]
        if start not in remain_ticket_map:
            remain_ticket_map[start] = [dest]
        else:
            remain_ticket_map[start].append(dest)
    # sort for consume ticket alphabetically sorted priority first
    for start in remain_ticket_map:
        remain_ticket_map[start].sort()
    return recursive_func(remain_ticket_map, 'ICN')[::-1]

def recursive_func(remain_ticket_map, start):
    # arrived in last destination we could go to
    if start not in remain_ticket_map or len(remain_ticket_map[start]) == 0:
        remain_cnt = sum([len(tickets) for tickets in remain_ticket_map.values()])
        return [start] if remain_cnt == 0 else None
    
    for idx in range(len(remain_ticket_map[start])):
        # consume current ticket for destination
        cur_dest = remain_ticket_map[start].pop(idx)
        route = recursive_func(remain_ticket_map, cur_dest)
        if route == None:
            # wrong. revert ticket to ticket_map
            remain_ticket_map[start].insert(idx, cur_dest)
            continue
        else:
            # collect. append own name and return to caller
            route.append(start)
            return route
    return None