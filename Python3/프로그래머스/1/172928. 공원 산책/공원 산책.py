
def solution(park, routes):
    # find starting point
    cur_pos = [0, 0]    
    for y_pos, line_str in enumerate(park):
        x_pos = line_str.find('S')
        if x_pos == -1:
            continue
        cur_pos = [y_pos, x_pos]
    
    # process move command
    for command in routes:
        direction, move_amount = command.split()
        move_amount = int(move_amount)

        result_pos = simulate_move(park, cur_pos, direction, move_amount)
        if direction == 'W' or direction == 'E':
            cur_pos[1] = result_pos
        else:
            cur_pos[0] = result_pos
            
    return cur_pos


def simulate_move(park, pos, direction, move_amount):
    is_side_step = (direction == 'E' or direction == 'W')
    dir_val = 1 if direction == 'E' or direction == 'S' else -1
    max_pos = (len(park[0]) if is_side_step else len(park)) -1
    
    fixed_pos = pos[0] if is_side_step else pos[1]
    origin_pos = pos[1] if is_side_step else pos[0]
    
    simulate_pos = origin_pos + dir_val
    dest_pos = origin_pos + (move_amount * dir_val)

    # out of range position
    if dest_pos < 0 or dest_pos > max_pos:
        return origin_pos

    # simulate while arrived to destination
    # simul == dest 여도 일단 검사 한 번 하고.
    while True:
        if (is_side_step and park[fixed_pos][simulate_pos] == 'X') \
            or (not is_side_step and park[simulate_pos][fixed_pos] == 'X'):
            return origin_pos
        if simulate_pos == dest_pos:
            break
        simulate_pos += dir_val

    return dest_pos
