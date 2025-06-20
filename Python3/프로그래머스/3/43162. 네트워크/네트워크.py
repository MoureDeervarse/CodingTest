def dfs_check(start_idx, computers, checked_indices):
    checked_indices.add(start_idx)
    for com_idx, is_connected in enumerate(computers[start_idx]):
        if is_connected == 0:
            # is not connected with computer of start_idx
            continue
        elif com_idx in checked_indices:
            # is already checked to visit
            continue
        else:
            dfs_check(com_idx, computers, checked_indices)

def solution(n, computers):
    network_count = 0
    checked_indices = set()
    for com_idx in range(n):
        if com_idx in checked_indices:
            continue
        
        dfs_check(com_idx, computers, checked_indices)
        network_count += 1
        
    return network_count
