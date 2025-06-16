def solution(wallpaper):
    min_x, min_y, max_x, max_y = len(wallpaper), len(wallpaper[0]), 0, 0 
    for row_idx, line_str in enumerate(wallpaper):
        for column_idx, word in enumerate(line_str):
            if word == '.':
                continue
            if column_idx < min_y:
                min_y = column_idx
            if column_idx > max_y:
                max_y = column_idx
            if row_idx < min_x:
                min_x = row_idx
            if row_idx > max_x:
                max_x = row_idx
    return [min_x, min_y, max_x + 1, max_y + 1]