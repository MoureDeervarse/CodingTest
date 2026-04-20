def solution(keyinput, board):
    answer = [0, 0]
    if len(keyinput) == 0:
        return answer
    
    if len(board) < 2:
        raise ValueError(f'Invalid board arary length {len(board)}')
    
    if board[0] % 2 == 0 or board[1] % 2 == 0:
        raise ValueError(f'Invalid board size number is not odd ([{board[0]}, {board[1]}])')
        
    max_x, max_y = max((board[0] - 1), 0) / 2, max((board[1] - 1), 0) / 2    
    for cmd in keyinput:
        if cmd == "left":
            answer[0] = get_moved_pos(answer[0], max_x, -1)
        elif cmd == "right":
            answer[0] = get_moved_pos(answer[0], max_x, 1)
        elif cmd == "up":
            answer[1] = get_moved_pos(answer[1], max_y, 1)
        elif cmd == "down":
            answer[1] = get_moved_pos(answer[1], max_y, -1)
        else:
            print(f'Invalid command {cmd}')
        
    return answer

def get_moved_pos(cur_pos, pos_limit, move_delta):
    if abs(cur_pos + move_delta) > pos_limit:
        return cur_pos
    return cur_pos + move_delta
    
    
    