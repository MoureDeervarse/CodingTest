import collections

def solution(maps):
    width, height = len(maps[0]), len(maps)
    target_pos_x, target_pos_y = width - 1, height - 1
    start_pos_x, start_pos_y = 0, 0
    
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)] # up down left right
    visited = [[False] * width for _ in range(height)]

    # set initial value
    queue = collections.deque([(start_pos_x, start_pos_y, 1)])
    visited[start_pos_y][start_pos_x] = True
    while queue:
        x, y, distance = queue.popleft()
        print(f"{x}, {y}, {distance}")
        if x == target_pos_x and y == target_pos_y:
            return distance
        
        for dir in directions:
            new_x, new_y = x + dir[0], y + dir[1]
            if not (0 <= new_x < width and 0 <= new_y < height):
                # out of range
                continue
            elif maps[new_y][new_x] == 0:
                # is blocked node
                continue
            elif visited[new_y][new_x]:
                # already visit the node
                continue
            else:
                # check visited and enqueue new node
                visited[new_y][new_x] = True            
                queue.append((new_x, new_y, distance + 1))

    # can not found the way to goal
    return -1