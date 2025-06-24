from functools import cmp_to_key

def solution(numbers):
    string_list = [str(num) for num in numbers]
    string_list.sort(key = cmp_to_key(lambda x, y: 1 if x + y < y + x else -1))

    result_str = ''.join(string_list)
    if result_str[0] == '0':
        return str(int(result_str))
    
    return result_str