def solution(n, lost, reserve):
    # organize list data to set for access with O(n) complexity
    set_reserve = set(reserve)
    set_lost = set({})
    for num in lost:
        # exclude duplicated value from each list
        if num in set_reserve:
            set_reserve.discard(num)
        else:
            set_lost.add(num)
    
    # check any extra clothes left around
    answer = n - len(set_lost)
    for lost_student in set_lost:
        if remove_from_set(set_reserve, lost_student - 1) \
            or remove_from_set(set_reserve, lost_student + 1):
            answer += 1
    return answer

def remove_from_set(set_reserve: set, check_student_num: int) -> bool:
    if check_student_num in set_reserve:
        set_reserve.discard(check_student_num)
        return True
    return False