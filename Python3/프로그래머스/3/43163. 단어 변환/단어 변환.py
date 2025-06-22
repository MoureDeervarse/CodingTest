def solution(begin, target, words):
    return check_func(begin, target, words, 0)

def check_func(current, target, words, count):
    if len(words) == 0:
        return 0
    
    succeed_results = []
    count += 1
    for w in words:
        if is_one_word_differ(current, w):
            if (target == w):
                return count
            new_word_list = words[:]
            new_word_list.remove(w)
            result = check_func(w, target, new_word_list, count)
            if result > 0:
                succeed_results.append(result)

    return min(succeed_results) if len(succeed_results) > 0 else 0
            
def is_one_word_differ(cur, new):
    different_cnt = 0
    for idx in range(len(cur)):
        if cur[idx] != new[idx]:
            different_cnt += 1
            if different_cnt > 1:
                return False
    return different_cnt == 1
